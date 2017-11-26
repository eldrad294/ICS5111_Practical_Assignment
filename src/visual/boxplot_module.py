import plotly.graph_objs as go
from plotly.offline import plot
import src.constants.string_consts as c
from src.preproc.preprocessing import Preprocessing
import src.constants.sql_consts as sql_c
#
def review_count_metrics(db_obj):
    """ Displays box plot metric of business review counts for those which are open. We set review_count < 50 to
    eliminate outlier data (ie: Businesses with review_counts so large they skew our data representation) """
    #
    sql = sql_c.sql_REVIEW_COUNT_METRICS
    df = db_obj.execute_query(sql)
    #
    review_count = []
    [(review_count.append(row[0])) for row in df]
    #
    # Normalize the data points
    #review_count = Preprocessing().normalize(review_count)
    #
    trace = go.Box(
        y=review_count
    )
    #
    data = [trace]
    layout = go.Layout(
        title=c.REVIEW_COUNT_METRICS,
        yaxis=dict(
            title='Review count variance'
        )
    )
    config = {'scrollZoom': True,
              'linkText': "Visit plot.ly"}
    fig = go.Figure(data=data, layout=layout)
    #
    # Plot and embed in ipython notebook!
    plot(fig, config=config)