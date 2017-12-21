import src.constants.sql_consts as sc
from src.db.database_handler import db
from src.textprocessing.SentimentAnalyzer_NB_NLTK import SentimentAnalyzer
from src.utils.json_formatter import json_formatter
import json
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
        self.jf = json_formatter('suggested_businesses.json')
    #
    def get_suggested_businesses(self, business_category, location, time, N):
        """
        The artifact's main callable function, is expected to return top N businesses (self.N).
        The return type should be in the form of a list of business dictionaries

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
        self.jf.suggested_businesses_to_json(business_cursor)
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
        n_step = 100
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