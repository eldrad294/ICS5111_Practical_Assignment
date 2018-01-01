#from src.textprocessing.SentimentAnalyzer_LogisticRegression import SentimentAnalyzer
#from src.textprocessing.SentimentAnalyzer_VADER import SentimentAnalyzer
from src.textprocessing.SentimentAnalyzer_NB import SentimentAnalyzer
sa = SentimentAnalyzer()
import json
#
class json_formatter():
    #
    def __init__(self):
        pass
    #
    def suggested_businesses_to_json(self, sql_cursor, path):
        """ Takes the sql cursor and formats it into a json string and saves it """
        json_string = "{\"businesses\":["
        for i, tuple in enumerate(sql_cursor):
            for json in tuple:
                if i == 0:
                    json_string += json
                else:
                    json_string += ',' + json
        json_string += ']}'
        self.save_json_to_path(json_string, path)
    #
    def business_cluster_to_json(self, sql_cursor, path):
        """ Takes the sql cursor and formats it into a json string and saves it """
        json_string = "{"
        for i, tuple in enumerate(sql_cursor):
            for json in tuple:
                if i == 0:
                    json_string += "\"" + str(i) + "\":" + json
                else:
                    json_string += ",\"" + str(i) + "\":" + json
        json_string += "}"
        self.save_json_to_path(json_string, path)
    #
    def business_user_graph_to_json(self, sql_cursor_nodes, sql_cursor_links, path):
        """ Takes the sql cursor and formats it into a json string and saves it. For the review links, sentiment
            analysis is performed on each review """
        n_step = 10000
        json_string = "{\"nodes\": ["
        for i, tuple in enumerate(sql_cursor_nodes):
            for json in tuple:
                if i == 0:
                    json_string += json
                else:
                    json_string += "," + json
        json_string += "], \"links\": ["
        #
        for i, tuple in enumerate(sql_cursor_links):
            sentence = tuple[2]
            pred = sa.predict(sentence)
            if pred == 'pos':
                color = 'blue'
            elif pred == 'neu':
                color = 'yellow'
            elif pred == 'neg':
                color = 'red'
            else:
                print('Unsupported Sentiment Type..exiting')
                exit(0)
            #
            if i == 0:
                json_string += "{\"source\": \"" + str(tuple[0]) + "\", \"target\": \"" + str(tuple[1]) + "\", \"type\": \"" + str(color) + "\", \"rv\": \"" + str(tuple[2]) + "\"}"
            else:
                json_string += ",{\"source\": \"" + str(tuple[0]) + "\", \"target\": \"" + str(tuple[1]) + "\", \"type\": \"" + str(color) + "\", \"rv\": \"" + str(tuple[2]) + "\"}"
            #
            if i % n_step == 0:
                print('Sentiment analysis on ' + str(i) + 'th review...')
        #
        json_string += "]}"
        #
        self.save_json_to_path(json_string, path)
    #
    # def save_json_to_path(self, json_string, path):
    #     """ Takes the json string and saves it to file """
    #     with open(path, 'w') as f:
    #         json.dump(json_string, f)
    def save_json_to_path(self, json_string, path):
        """ Takes the json string and saves it to file """
        with open(path, 'w') as f:
            f.write(json_string)