import src.constants.sql_consts as sc
from src.db.database_handler import db
from src.textprocessing.SentimentAnalyzer_LogisticRegression import SentimentAnalyzer
from src.utils.json_formatter import json_formatter
from src.utils.word_bucket import Word_Bucket
#
class Core():
    #
    """
    Example:

    from src.db.core import Core
    c = Core('restaurant', [43.8409,-79.3996])
    c.populate_table_business_user_sentiment()
    """
    def __init__(self):
        self.db_obj = db('127.0.0.1', 'yelp_db', 'root', '1234')
        self.sa = SentimentAnalyzer()
        self.jf = json_formatter()
        self.wb = Word_Bucket()
    #
    def get_suggested_businesses(self, business_category, location, time, N):
        """
        Creates a json file consisting of top N businesses (self.N).
        The function creates a json file based on the output of the query results

        1) Category: Defines the type of business category the user is looking for
        2) Location: Current user location, expected in the form of a [longitude,latitude]
        3) N: Total number of businesses to be returned in surrounding area
        """
        #
        # Input validation
        business_category = business_category.title()
        sentiment_threshold = 1
        #
        # Establish database connection
        conn = self.db_obj.connect()
        sql = sc.sql_BUSINESS_USER_SENTIMENT(business_category, location, sentiment_threshold, time, N)
        #
        # Retrieve businesses
        print('Retrieving businesses in near vicinity ' + str(location[0]) + ',' + str(location[1]) + '...')
        business_cursor = self.db_obj.select_query(conn, sql)
        #
        # Closes database connection
        self.db_obj.close(conn)
        #
        # Return cursor as JSON format
        self.jf.suggested_businesses_to_json(business_cursor, 'yelp.json')
    #
    def get_business_cluster(self, cluster_category="city"):
        """ Creates a json file consisting of hexagonal clustering of businesses as defined by the cluster_category, which must be the following:
            1) neighborhood
            2) city
            3) state
        """
        #
        # Input formatting
        cluster_category = cluster_category.lower()
        #
        # Establish database connection
        conn = self.db_obj.connect()
        #
        if cluster_category == 'neighborhood':
            sql = sc.sql_BUSINESS_CLUSTERING_NEIGHBORHOOD
        elif cluster_category == 'city':
            sql = sc.sql_BUSINESS_CLUSTERING_CITY
        elif cluster_category == 'state':
            sql = sc.sql_BUSINESS_CLUSTERING_STATE
        else:
            print('Unsupported cluster category')
            exit()
        #
        # Retrieving clusters
        print('Retrieving business clusters...')
        cluster_cursor = self.db_obj.select_query(conn, sql)
        #
        # Closes database connection
        self.db_obj.close(conn)
        #
        # Return cursor as JSON format
        self.jf.business_cluster_to_json(cluster_cursor, cluster_category + '_geo.json')
    #
    def get_business_user_graph(self, business_category='Food',city='OH', business_name=None):
        """ Creates a json file consisting of Business Node Clusters with respect to users """
        #
        # Input formatting
        business_category = business_category.lower()
        city = city.upper()
        #
        # Establish database connection
        conn = self.db_obj.connect()
        #
        if business_name is None:
            sql = sc.sql_BUSINESS_USER_NODES(city, business_category)
            sql2 = sc.sql_BUSINESS_USER_LINKS(city, business_category)
        else:
            pass
        #
        # Retrieving business user nodes
        print('Retrieving business user nodes cursor...')
        business_user_nodes_cursor = self.db_obj.select_query(conn, sql)
        #
        # Retrieving business user links
        print('Retrieving business user links cursor...')
        business_user_links_cursor = self.db_obj.select_query(conn, sql2)
        #
        # Closes database connection
        self.db_obj.close(conn)
        #
        # Return cursor as JSON format
        self.jf.business_user_graph_to_json(business_user_nodes_cursor, business_user_links_cursor, 'graph.json')
        #
        print('JSON file successfully created!')
    #
    def populate_table_business_user_sentiment(self, city):
        """
        This method carries out sentiment analysis on user reviews per business, and calculates a sentiment value
        vector to assign to a particular business. It then goes over every business which had sentiment analysis
        performed on it and updates table BUSINESS_USER_SENTIMENT
        """
        print("Started sentiment analysis on state " + str(city))
        #
        # Establish database connection
        conn = self.db_obj.connect()
        #
        sql = sc.sql_REVIEW_BUSINESS_AND_TEXT(city.upper())
        #
        # Retrieve businesses
        print('Retrieving Yelp reviews...')
        review_cursor = self.db_obj.select_query(conn, sql)
        #
        # Closes database connection
        self.db_obj.close(conn)
        #
        # Iterate over retrieved records and perform sentiment analysis
        counter = 0
        review_dict = dict()
        n_step = 1000
        print('Commencing review sentiment analysis...')
        for id, text in review_cursor:
            #
            sentiment_vector = 0
            sentiment = self.sa.predict(text)
            if sentiment == 'pos':
                sentiment_vector += 1
            elif sentiment == 'neg':
                sentiment_vector -= 1
            else:
                pass # We do not update sentiment_vector for neutral reviews
            #
            if id in review_dict:
                review_dict[id] += sentiment_vector
            else:
                review_dict[id] = 0 + sentiment_vector
            #
            counter += 1
            if counter % n_step == 0:
                print('Sentiment analysis on ' + str(counter) + 'th review...')
        #
        counter = 0
        print('Commencing business updates...')
        #
        # Establish database connection
        conn = self.db_obj.connect()
        #
        for id, sentiment_vector in review_dict.items():
            #
            sql = sc.sql_UPDATE_BUSINESS(sentiment_vector, id)
            self.db_obj.execute_query(conn, sql)
            #
            counter += 1
            #
            if counter % n_step == 0:
                print(str(counter) + 'th business updated...')
        #
        # Closes database connection
        self.db_obj.close(conn)
        #
        print('Sentiment Analysis performed on ' + city + " done!!")
    #
    def get_top_N_trending_words(self, user_id, N=10, pos=False):
        """ Returns the top N trending words used in either reviews and/or tips """
        #
        print('Returning all text pertaining to user: ' + str(user_id))
        #
        # Establish database connection
        conn = self.db_obj.connect()
        #
        sql = sc.sql_REVIEW_TEXT_PER_USER(user_id)
        #
        sql_cursor = self.db_obj.select_query(conn, sql)
        #
        # Closes database connection
        self.db_obj.close(conn)
        #
        agglomorated_text = ''
        for i, tuple in enumerate(sql_cursor):
            for text in tuple:
                agglomorated_text += text + " "
        #
        keys, values = self.wb.get_top_N_frequent_words(agglomorated_text, N, pos)
        #
        top_N_words = ""
        for i in range(1,len(keys)):
            if i == N:
                top_N_words += str(keys[i])
            else:
                top_N_words += str(keys[i]) + ","
        return top_N_words
    #
    def data_mine_top_N_users(self, N=500, top_trending_word_count=20, pos=False):
        """ Constructs 2 JSON files for the top N users, one consisting of user estimated living coordinates, and
            another with a users trace history """
        #
        print("Started data mining task on top " + str(N) + " users..")
        #
        # Establish database connection
        conn = self.db_obj.connect()
        #
        sql = sc.sql_RETRIEVE_TOP_N_USERS(N)
        sql_cursor = self.db_obj.select_query(conn, sql)
        print('Retrieved top ' + str(N) + ' users..')
        #
        user_datamined_data, top_N_user_words, user_history = [],[], []
        for i, tuple in enumerate(sql_cursor):
            for user_id in tuple:
                #
                print('Commencing datamining on user: ' + str(user_id))
                sql = sc.sql_USER_DATA_MINE(user_id)
                sql_cursor2 = self.db_obj.select_query(conn, sql)
                user_datamined_data.append(sql_cursor2)
                #
                # Returns top N trending words by user
                print('Retrieving top trending words..')
                top_N_user_words.append(self.get_top_N_trending_words(user_id, top_trending_word_count, pos))
                #
                print('Retrieving user history')
                sql = sc.sql_USER_HISTORY(user_id)
                sql_cursor2 = self.db_obj.select_query(conn, sql)
                user_history.append(sql_cursor2)
        #
        # Closes database connection
        self.db_obj.close(conn)
        #
        print('Data Mining Task Complete, commencing JSON serializing')
        #
        # Pass lists to be converted into JSON files
        self.jf.user_data_mined_to_json(user_datamined_data, top_N_user_words, 'user_datamined.json')
        self.jf.user_history_to_json(user_history, 'user_history.json')
        self.jf.generate_word_graph_template(top_N_user_words, 'user_word_cloud.json')
        #
        print('JSON files successfully created!')
