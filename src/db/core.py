class Core():
    #
    def __init__(self, business_category, location):
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
        pass