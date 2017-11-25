import plotly.graph_objs as go
from plotly.offline import plot
from plotly.graph_objs import *
import src.constants.consts as c
#
def display_business_distribution_over_states(db_obj):
    """" Displays a spread of businesses distributed per state """
    #
    sql = "select count(state), state from yelp_db.business group by state;"
    df = db_obj.execute_query(sql)
    #
    states,state_count = [],[]
    [(state_count.append(row[0]), states.append(row[1])) for row in df]
    #
    data = Data([
        Bar(
            x=states,
            y=state_count
        )
    ])
    layout = go.Layout(
        title=c.BUSINESS_DISTRIBUTION_OVER_STATES,
    )
    config = {'scrollZoom': True,
              'linkText': "Visit plot.ly"}
    fig = go.Figure(data=data, layout=layout)
    plot(fig, config=config)
#