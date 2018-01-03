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
                json_string += "{\"source\": \"" + str(tuple[0]) + "\", \"target\": \"" + str(tuple[1]) + "\", \"type\": \"" + str(color) + "\", \"rv\": \"" + str(tuple[2]).replace('"','') + "\"}"
                #json_string += "{\"source\": \"" + str(tuple[0]) + "\", \"target\": \"" + str(tuple[1]) + "\", \"type\": \"" + str(color) + "\", \"rv\": \"review\"}"
            else:
                json_string += ",{\"source\": \"" + str(tuple[0]) + "\", \"target\": \"" + str(tuple[1]) + "\", \"type\": \"" + str(color) + "\", \"rv\": \"" + str(tuple[2]).replace('"','') + "\"}"
                #json_string += ",{\"source\": \"" + str(tuple[0]) + "\", \"target\": \"" + str(tuple[1]) + "\", \"type\": \"" + str(color) + "\", \"rv\": \"review\"}"
            #
            if i % n_step == 0:
                print('Sentiment analysis on ' + str(i) + 'th review...')
        #
        json_string += "]}"
        #
        self.save_json_to_path(json_string, path)
    #
    def user_data_mined_to_json(self, user_datamined_data, top_N_user_words, path):
        """ Takes the sql cursor and formats it into a json string and saves it. """
        #
        json_string = '{"users": ['
        for i, tuple in enumerate(user_datamined_data):
            if i == 0:
                json_string += '{"user_id":"' + str(tuple[0][0]) + '","name":"' + str(tuple[0][1]) + '", "latitude":' + str(
                    tuple[0][2]) + ',"longitude":' + str(tuple[0][3]) + ',"financial_status":"' + str(
                    tuple[0][4]) + '", "city":"' + str(tuple[0][5]) + '", "personality_trait_dubbed_by_reviewers":"' + str(
                    tuple[0][6]) + '","fans":' + str(tuple[0][7]) + ',"review_count":' + str(
                    tuple[0][8]) + ',"review_rating":' + str(tuple[0][9]) + ',"trending_compliments":"' + str(
                    tuple[0][10]) + '","top_20_words":"' + str(top_N_user_words[i]) + '"}'
            else:
                json_string += ',{"user_id":"' + str(tuple[0][0]) + '","name":"' + str(tuple[0][1]) + '", "latitude":' + str(
                    tuple[0][2]) + ',"longitude":' + str(tuple[0][3]) + ',"financial_status":"' + str(
                    tuple[0][4]) + '", "city":"' + str(tuple[0][5]) + '", "personality_trait_dubbed_by_reviewers":"' + str(
                    tuple[0][6]) + '","fans":' + str(tuple[0][7]) + ',"review_count":' + str(
                    tuple[0][8]) + ',"review_rating":' + str(tuple[0][9]) + ',"trending_compliments":"' + str(
                    tuple[0][10]) + '","top_20_words":"' + str(top_N_user_words[i]) + '"}'
        json_string += ']}'
        #
        self.save_json_to_path(json_string, path)
    def user_history_to_json(self, user_history, path):
        """ Takes the sql cursor and formats it into a json string and saves it. """
        #
        json_string = '{"user_history": ['
        #
        for i, tuple in enumerate(user_history):
            if i == 0:
                json_string += '{"user_id":"' + str(tuple[0][0]) + '","state":"' + str(tuple[0][1]) + '","city":"' + str(
                    tuple[0][2]) + '","neighborhood":"' + str(tuple[0][3]) + '","latitude":' + str(
                    tuple[0][4]) + ',"longitude":' + str(tuple[0][5]) + ',"address":"' + str(tuple[0][6]) + '","name":"' + str(
                    tuple[0][7]) + '","date":"' + str(tuple[0][8]) + '"}'
            else:
                json_string += ',{"user_id":"' + str(tuple[0][0]) + '","state":"' + str(tuple[0][1]) + '","city":"' + str(
                    tuple[0][2]) + '","neighborhood":"' + str(tuple[0][3]) + '","latitude":' + str(
                    tuple[0][4]) + ',"longitude":' + str(tuple[0][5]) + ',"address":"' + str(tuple[0][6]) + '","name":"' + str(
                    tuple[0][7]) + '","date":"' + str(tuple[0][8]) + '"}'
        json_string += ']}'
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