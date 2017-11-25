import src.visual.bar_module as bm
import src.visual.scatter_module as sm
from src.db.database_handler import db
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
        #
        bm.display_business_distribution_over_states(self.db_obj)
    #
    def scatter_handler(self):
        """ A wrapper function which calls/encompasses the scatter plot visuals """
        #
        pass
    #
    def get_help(self):
        return help(plotly.offline.plot)