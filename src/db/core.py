import src.constants.sql_consts as sc
from src.db.database_handler import db
from src.textprocessing.SentimentAnalyzer_NB_NLTK import SentimentAnalyzer
#
class Core():
    #
    def __init__(self, business_category, location):
        self.db_obj = db('127.0.0.1', 'yelp_db', 'root', '1234')
        self.sa = SentimentAnalyzer()
        self.business_category = business_category # Defines the type of business category the user is looking for
        self.location = location # Current user location, expected in the form of a [longitude,latitude]
        self.N = 10 # Total number of businesses to be returned in surrounding area
    #
    def get_suggested_businesses(self):
        """ The artifact's main callable function, is expected to return top N businesses (self.N).
        The return type should be in the form of a list of business dictionaries """
        pass
    #
    def populate_table_business_user_sentiment(self):
        """ This method carries out sentiment analysis on user reviews per business, and calculates a sentiment value
        vector to assign to a particular business """
        #
        sql = sc.sql_REVIEW_BUSINESS_AND_TEXT
        #
        # Retrieve businesses
        print('---Retrieving Yelp reviews---')
        review_cursor = self.db_obj.select_query(sql)
        #
        # Iterate over retrieved records and perform sentiment analysis
        counter = 0
        review_dict = dict()
        n_step = 100
        print('---Commencing review sentiment analysis---')
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
                print('Sentiment analysis on ' + str(counter) + 'th review')
        #
        counter = 0
        print('---Commencing business updates---')
        for id, sentiment_vector in review_dict.items():
            #
            sql = sc.sql_UPDATE_BUSINESS(sentiment_vector, id)
            self.db_obj.execute_query(sql)
            #
            counter += 1
            #
            if counter % n_step == 0:
                print('---' + str(counter) + 'th business updated---')