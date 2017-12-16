import src.visual.bar_module as bm
import src.visual.scatter_module as sm
from src.db.database_handler import db
import src.visual.boxplot_module as bph
import src.visual.pie_module as ph
import plotly
#
class visual():
    #
    """ A handler class, through which all the visualizing functions can be handled/executed from. """
    def __init__(self):
        self.db_obj = db('127.0.0.1', 'yelp_db', 'root', '1234')
    #
    def bar_handler(self):
        """ A wrapper function which calls/encompasses the bar graph visuals """
        # #
        # bm.display_business_distribution_over_states(self.db_obj)
        # #
        # bm.business_rating_vs_review_count(self.db_obj)
        # #
        # bm.photo_labels_vs_count(self.db_obj)
        #
        bm.review_sentiment(self.db_obj)
        # #
        # bm.yelp_elite_over_time(self.db_obj)
    #
    def scatter_handler(self):
        """ A wrapper function which calls/encompasses the scatter plot visuals """
        #
        pass
    #
    def boxplot_handler(self):
        """ A wrapper function which calls/encompasses the boxplot graph visuals """
        #
        bph.review_count_metrics(self.db_obj)
    #
    def pieplot_handler(self):
        """ A wrapper function which calls/encompasses the pie graph visuals """
        #
        ph.display_business_distribution_over_states(self.db_obj)
    #
    def get_help(self):
        return help(plotly.offline.plot)