from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from src.textprocessing.Scoring_Functions import Scoring_Functions
from src.textprocessing.Word_Corpus import WordCorpus
from src.textprocessing.Text_Cleanup import TextCleanup
#
# https://medium.com/@aneesha/quick-social-media-sentiment-analysis-with-vader-da44951e4116
class SentimentAnalyzer():
    #
    """ An example as to how invoke and use this class:
            from src.textprocessing.SentimentAnalyzer import SentimentAnalyzer
            sa = SentimentAnalyzer()
            pred = sa.predict("I will never go there again")
            print(pred)
    """
    def __init__(self):
        self.text_cleanup = TextCleanup()
        self.sid = SIA()
        self.__word_corpus = WordCorpus()
    #
    def predict(self,sentence):
        """ Public function. Takes a sentence as parameter and assigns a sentiment label to it (pos/neg/neu) """
        #
        # filtered_words = self.text_cleanup.clean_sentence(sentence)
        # polarity = self.sid.polarity_scores(' '.join(filtered_words))
        #
        polarity = self.sid.polarity_scores(sentence)
        sentiment = ""
        sentiment_score = -1
        for key, val in polarity.items():
            if val > sentiment_score and key != "compound":
                sentiment = key
                sentiment_score = val
        print(sentence)
        print(sentiment)
        print('---------------------------')
        return sentiment
    #
    def test_set(self):
        """ Public function. Uses the classifier on the testing set of data to determine the accuracy """
        #
        y_pred, y_true = [], []
        test_sentences, y_true = self.__word_corpus.get_test_corpus()
        #
        [(y_pred.append(self.predict(sentence))) for sentence in test_sentences]
        #
        score_func = Scoring_Functions(y_pred, y_true)
        accuracy = score_func.accuracy()
        precision = score_func.precision()
        recall = score_func.recall()
        f_measure = score_func.f_measure()
        return "Accuracy: " + str(accuracy) + "\nPrecision: " + str(precision) + "\nRecall: " + str(recall) + "\nF_Measure: " + str(f_measure)