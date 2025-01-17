import plotly.graph_objs as go
from plotly.offline import plot

import src.constants.sql_consts as sql_c
import src.constants.string_consts as c
#
def display_business_distribution_over_states(db_obj, conn):
    """" Displays a spread of top 15 states with highest business count """
    #
    # Open database connection
    conn = db_obj.connect()
    #
    sql = sql_c.sql_BUSINESS_DISTRIBUTION_OVER_STATES
    df = db_obj.select_query(conn, sql)
    #
    # Close database connection
    db_obj.close(conn)
    #
    states,state_count = [],[]
    [(state_count.append(row[0]), states.append(row[1])) for row in df]
    #
    trace = go.Pie(labels=states, values=state_count)
    data = [trace]
    layout = go.Layout(
        title=c.BUSINESS_DISTRIBUTION_OVER_STATES,
    )
    config = {'linkText': "Visit plot.ly"}
    fig = go.Figure(data=data, layout=layout)
    plot(fig, config=config)