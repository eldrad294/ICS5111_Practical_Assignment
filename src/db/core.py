import src.constants.sql_consts as sc
from src.db.database_handler import db
from src.textprocessing.SentimentAnalyzer_NB import SentimentAnalyzer
from src.utils.json_formatter import json_formatter
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
    def get_business_user_graph(self, business_category='Food',state='OH', business_name=None):
        """ Creates a json file consisting of Business Node Clusters with respect to users """
        #
        # Input formatting
        business_category = business_category.lower()
        state = state.upper()
        #
        # Establish database connection
        conn = self.db_obj.connect()
        #
        if business_name is None:
            sql = sc.sql_BUSINESS_USER_NODES(state, business_category)
            sql2 = sc.sql_BUSINESS_USER_LINKS(state, business_category)
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
        # Perform Sentiment Analysis on link reviews
        #
        # Closes database connection
        self.db_obj.close(conn)
        #
        # Return cursor as JSON format
        self.jf.business_user_graph_to_json(business_user_nodes_cursor, business_user_links_cursor, 'graph.json')
    #
    def populate_table_business_user_sentiment(self):
        """
        This method carries out sentiment analysis on user reviews per business, and calculates a sentiment value
        vector to assign to a particular business. It then goes over every business which had sentiment analysis
        performed on it and updates table BUSINESS_USER_SENTIMENT
        """
        #
        # Establish database connection
        conn = self.db_obj.connect()
        #
        sql = sc.sql_REVIEW_BUSINESS_AND_TEXT
        #
        # Retrieve businesses
        print('Retrieving Yelp reviews...')
        review_cursor = self.db_obj.select_query(conn, sql)
        #
        # Iterate over retrieved records and perform sentiment analysis
        counter = 0
        review_dict = dict()
        n_step = 10000
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
            if text in review_dict:
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