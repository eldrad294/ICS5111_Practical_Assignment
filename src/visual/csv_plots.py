import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import numpy as np
#
class csv_plots():
    #
    def __init__(self):
        pass
    #
    def N_of_user_comments_distribution_per_business_states(self):
        """ Bar graphs """
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/N on reviews distribution per business states.csv')
        rev_count = df['count(*)'].values
        states = df['state'].values
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/N on tips distribution per state.csv')
        tip_count = df['count(*)'].values
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/N on photo caption distribution per state.csv')
        photo_count = df['count(*)'].values
        #
        trace1 = go.Bar(
            x=states,
            y=rev_count,
            name='reviews'
        )
        trace2 = go.Bar(
            x=states,
            y=tip_count,
            name='tips'
        )
        trace3 = go.Bar(
            x=states,
            y=photo_count,
            name='photo captions'
        )
        data = [trace1, trace2, trace3]
        layout = go.Layout(
            title="N_of_user_comments_distribution_per_business_states",
            xaxis=dict(
                title='States'
            ),
            yaxis=dict(
                title='Count'
            ),
            barmode='group'
        )
        config = {'scrollZoom': True,
                  'linkText': "Visit plot.ly"}
        fig = go.Figure(data=data, layout=layout)
        plot(fig, config=config)
    #
    def N_of_primary_categories(self):
        """ Bar graphs """
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/N of primary_category.csv')
        count = df['count(*)'].values
        category = df['primary_category'].values
        #
        trace1 = go.Bar(
            x=category,
            y=count,
            name='primary categories'
        )
        data = [trace1]
        #
        layout = go.Layout(
            title="N_of_primary_categories",
            xaxis=dict(
                title='Primary Categories'
            ),
            yaxis=dict(
                title='Count'
            ),
            barmode='bar'
        )
        config = {'scrollZoom': True,
                  'linkText': "Visit plot.ly"}
        fig = go.Figure(data=data, layout=layout)
        plot(fig, config=config)
    #
    def N_of_secondary_categories(self):
        """ Bar graphs """
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/N of secondary_category.csv')
        count = df['count(*)'].values
        category = df['secondary_category'].values
        #
        trace1 = go.Bar(
            x=category,
            y=count,
            name='secondary categories'
        )
        data = [trace1]
        #
        layout = go.Layout(
            title="N_of_secondary_categories",
            xaxis=dict(
                title='Secondary Categories'
            ),
            yaxis=dict(
                title='Count'
            ),
            barmode='bar'
        )
        config = {'scrollZoom': True,
                  'linkText': "Visit plot.ly"}
        fig = go.Figure(data=data, layout=layout)
        plot(fig, config=config)
    #
    def retrieve_comment_distribution_by_category(self):
        """ Bar graphs """
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/Retrieve review distribution by category.csv')
        rev_count = df['review_counts'].values
        category = df['category'].values
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/Retrieve tip distribution by category.csv')
        tip_count = df['tip_counts'].values
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/Retrieve photo caption distribution by category.csv')
        photo_count = df['category'].values
        #
        trace1 = go.Bar(
            x=category,
            y=rev_count,
            name='reviews'
        )
        trace2 = go.Bar(
            x=category,
            y=tip_count,
            name='tips'
        )
        trace3 = go.Bar(
            x=category,
            y=photo_count,
            name='photo captions'
        )
        data = [trace1, trace2, trace3]
        layout = go.Layout(
            title="Comment distribution by category",
            xaxis=dict(
                title='Categories'
            ),
            yaxis=dict(
                title='Counts'
            ),
            barmode='group'
        )
        config = {'scrollZoom': True,
                  'linkText': "Visit plot.ly"}
        fig = go.Figure(data=data, layout=layout)
        plot(fig, config=config)
    #
    def user_comments_over_time(self):
        """ Line graph """
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/Review counts distribution per day over time.csv')
        rev_count = df['rev_count'].values
        date = df['date'].values
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/User tips per day.csv')
        tip_count = df['tips'].values
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/User yelping_since signups per day.csv')
        user_signup = df['user_signup'].values
        yelping_since = df['yelping_since'].values
        #
        trace1 = go.Scatter(
            x=date,
            y=rev_count,
            name='reviews'
        )
        trace2 = go.Scatter(
            x=date,
            y=tip_count,
            name='tips'
        )
        trace3 = go.Scatter(
            x=yelping_since,
            y=user_signup,
            name='user signups'
        )
        data = [trace1, trace2, trace3]
        layout = go.Layout(
            title="Comment distribution over time",
            xaxis=dict(
                title='Timeline'
            ),
            yaxis=dict(
                title='Counts'
            ),
            barmode='basic-line'
        )
        config = {'scrollZoom': True,
                  'linkText': "Visit plot.ly"}
        fig = go.Figure(data=data, layout=layout)
        plot(fig, config=config)
    #
    def Average_review_length_per_star_rating(self):
        """ Bar graphs """
        df = pd.read_csv('../data analysis/Review Analysis/data_extracts/Average review length per star rating.csv')
        avg_length = df['avg(length(text))'].values
        stars = df['stars'].values
        #
        trace1 = go.Bar(
            x=stars,
            y=avg_length,
            name='review_text'
        )
        data = [trace1]
        layout = go.Layout(
            title="Average review length per star rating",
            xaxis=dict(
                title='Star ratings'
            ),
            yaxis=dict(
                title='Average text length'
            ),
            barmode='bar'
        )
        config = {'scrollZoom': True,
                  'linkText': "Visit plot.ly"}
        fig = go.Figure(data=data, layout=layout)
        plot(fig, config=config)