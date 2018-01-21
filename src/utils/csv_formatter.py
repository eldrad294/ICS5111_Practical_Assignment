#from src.textprocessing.SentimentAnalyzer_LogisticRegression import SentimentAnalyzer
from src.textprocessing.SentimentAnalyzer_VADER import SentimentAnalyzer
#from src.textprocessing.SentimentAnalyzer_NB import SentimentAnalyzer
sa = SentimentAnalyzer()
class csv_formatter():
    #
    def __init__(self):
        pass
    #
    def generate_word_graph_template(self, top_N_user_words, path):
        """ Generates word cloud json file """
        #
        review_dict = dict()
        #
        for word_sentence in top_N_user_words:
            word_list = word_sentence.split(",")
            for word in word_list:
                if word in review_dict:
                    review_dict[word] += 1
                else:
                    review_dict[word] = 1
        #
        csv_list = []
        for word, value in review_dict.items():
            pred = sa.predict(word)
            csv_list.append([word, pred, value])
        #
        self.save_csv_to_path(csv_list, path)
    #
    def save_csv_to_path(self, csv_list, path):
        """ Takes the json string and saves it to file """
        try:
            with open(path, 'w', encoding='utf-8') as f:
                for line in csv_list:
                    f.write(str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]))
                    f.write('\n')
        except Exception as e:
            print(str(e))