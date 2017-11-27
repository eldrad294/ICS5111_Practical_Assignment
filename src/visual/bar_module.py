import plotly.graph_objs as go
from plotly.offline import plot
from plotly.graph_objs import *
import src.constants.string_consts as c
import src.constants.sql_consts as sql_c
from src.textprocessing.SentimentAnalyzer import SentimentAnalyzer
from threading import Thread
#
sentiment_count_results = []
#
def display_business_distribution_over_states(db_obj):
    """" Displays a spread of businesses distributed per state """
    #
    sql = sql_c.sql_BUSINESS_DISTRIBUTION_OVER_STATES_2
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
        xaxis=dict(
            title='States'
        ),
        yaxis=dict(
            title='Business Count'
        )
    )
    config = {'scrollZoom': True,
              'linkText': "Visit plot.ly"}
    fig = go.Figure(data=data, layout=layout)
    plot(fig, config=config)
#
def business_rating_vs_review_count(db_obj):
    """ Displays business star rating vs the amount of review counts per business (which are still active)"""
    #
    sql = sql_c.sql_BUSINESS_RATING_VS_REVIEW_COUNT
    df = db_obj.execute_query(sql)
    #
    stars, review_count = [], []
    [(stars.append(row[0]), review_count.append(row[1])) for row in df]
    #
    data = Data([
        Bar(
            x=stars,
            y=review_count
        )
    ])
    layout = go.Layout(
        title=c.BUSINESS_RATING_VS_REVIEW_COUNT,
        xaxis=dict(
            title='Business Rating'
        ),
        yaxis=dict(
            title='Number of Reviews'
        )
    )
    config = {'scrollZoom': True,
              'linkText': "Visit plot.ly"}
    fig = go.Figure(data=data, layout=layout)
    #
    # Plot and embed in ipython notebook!
    plot(fig, config=config)
#
def photo_labels_vs_count(db_obj):
    """ Displays photo label/genre vs respective count """
    #
    sql = sql_c.sql_PHOTO_CATEGORIZED_BY_LABEL
    df = db_obj.execute_query(sql)
    #
    label_cnt, label = [], []
    [(label_cnt.append(row[0]), label.append((row[1]))) for row in df]
    #
    data = Data([
        Bar(
            x=label,
            y=label_cnt
        )
    ])
    layout = go.Layout(
        title=c.PHOTO_CATEGORIZED_BY_LABEL,
        xaxis=dict(
            title='Label Genre'
        ),
        yaxis=dict(
            title='Photo Count'
        )
    )
    config = {'scrollZoom': True,
              'linkText': "Visit plot.ly"}
    fig = go.Figure(data=data, layout=layout)
    #
    # Plot and embed in ipython notebook!
    plot(fig, config=config)
#
def review_sentiment(db_obj):
    """ Displays review sentiment based on positive/negative/neutral reviews """
    #
    threads = []
    sentiment_text = ['pos', 'neg', 'neu']
    #
    # We initiate n number of jobs ranging from 2004 till 2017
    for i in range(2004, 2017):
        sql_filter = ' where date like \'' + str(i) + '%\' LIMIT 1000;'
        process = Thread(target=review_sentiment_counter, args=[db_obj,sql_filter, sentiment_text, i])
        process.start()
        threads.append(process)
    #
    #
    # We wait for all threads to finish
    for process in threads:
        process.join()
    #
    sentiment_counts, s1, s2, s3 = [],[],[],[]
    [(s1.append(row[0]),s2.append(row[1]),s3.append(row[2])) for row in sentiment_count_results]
    sentiment_counts.append(sum(s1))
    sentiment_counts.append(sum(s2))
    sentiment_counts.append(sum(s3))
    #
    data = Data([
        Bar(
            x=sentiment_text,
            y=sentiment_counts
        )
    ])
    layout = go.Layout(
        title=c.REVIEW_SENTIMENT,
        xaxis=dict(
            title='Sentiment Category'
        ),
        yaxis=dict(
            title='Sentiment Count'
        )
    )
    config = {'scrollZoom': True,
              'linkText': "Visit plot.ly"}
    fig = go.Figure(data=data, layout=layout)
    #
    # Plot and embed in ipython notebook!
    plot(fig, config=config)
#
def review_sentiment_counter(db_obj, sql_filter, sentiment_text, year):
    """ An executable function which allows for parallel counting of sentiment analysis """
    #
    sql = sql_c.sql_REVIEWS + sql_filter
    df = db_obj.execute_query(sql)
    #
    review_texts = []
    [(review_texts.append(row[0])) for row in df]
    #
    sa = SentimentAnalyzer()
    sentiment_counts = [0,0,0] # pos, neg, neu
    #
    # Perform sentiment analysis and return counts in 3 buckets
    for i, text in enumerate(review_texts):
        if i % 1000 == 0:
            print('Performing sentiment analysis for year ' + str(year) + '... ' + str(i) + " records processed.")
        sentiment = sa.predict(text)
        if sentiment == sentiment_text[0]:
            sentiment_counts[0] += 1
        elif sentiment == sentiment_text[1]:
            sentiment_counts[1] += 1
        elif sentiment == sentiment_text[2]:
            sentiment_counts[2] += 1
        else:
            print("Unhandled value. Terminate @review_sentiment()")
    #
    # We assign the count values to the original list we passed, in order for the thread to return an output
    sentiment_count_results.append(sentiment_counts)
