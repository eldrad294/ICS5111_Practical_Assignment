from nltk.classify import NaiveBayesClassifier
from nltk import precision
from sklearn.naive_bayes import MultinomialNB
from src.textprocessing.Word_Corpus import WordCorpus
from sklearn.metrics import accuracy_score
from src.textprocessing.Text_Cleanup import TextCleanup
from src.textprocessing.Scoring_Functions import Scoring_Functions
#
class SentimentAnalyzer():
    #
    """
    Example:

    from src.textprocessing.SentimentAnalyzer import SentimentAnalyzer
    sa = SentimentAnalyzer()
    pred = sa.predict("I will never go there again")
    print(pred)
    """
    def __init__(self):
        self.__word_corpus = WordCorpus()
        train_set = self.__format_vocab()
        self.__NBclassifier = self.__train_classifier(train_set)
        self.text_cleanup = TextCleanup()
    #
    def __word_feats(self, words):
        """ Takes a word and converts it into a python dictionary """
        return dict([(words.lower(), True)])
    #
    def __format_vocab(self):
        """ Returns an entire set of vocab which is marked as either 1) Positive, 2) Negative, 3) Neutral for NLTK
        classification """
        positive_vocab, negative_vocab, neutral_vocab = self.__word_corpus.get_vocab()
        #
        positive_features = [(self.__word_feats(str(pos)), 'pos') for pos in positive_vocab]
        negative_features = [(self.__word_feats(str(neg)), 'neg') for neg in negative_vocab]
        neutral_features = [(self.__word_feats(str(neu)), 'neu') for neu in neutral_vocab]
        #
        return positive_features + negative_features + neutral_features
    #
    def __train_classifier(self, train_set, train_labels=None):
        """ Takes the training vocab (consisting of pos,neg,neu) vocab and trains itself """
        #
        # NLTK's Naive Bayes classifier.
        #print(train_set)
        return NaiveBayesClassifier.train(train_set)
    #
    def __classify(self, word):
        """ Takes input sample and classifies it as either pos / neu / neg """
        #
        # NLTK Naive Bayes Classification
        return self.__NBclassifier.classify(self.__word_feats(word))
    #
    def predict(self,sentence):
        """ Public function. Takes a sentence as parameter and assigns a sentiment label to it (pos/neg/neu) """
        pos,neg,neu = 0,0,0
        #
        filtered_words = self.text_cleanup.clean_sentence(sentence)
        #self.__NBclassifier.show_most_informative_features()
        for word in filtered_words:
            prediction = self.__classify(word)
            #print(str(word) + " - " + str(prediction))
            if prediction == "pos":
                pos += 1
            elif prediction == "neg":
                neg += 1
            elif prediction == "neu":
                neu += 1
        #
        # print('-----------------')
        # print(pos)
        # print(neu)
        # print(neg)
        if pos > neg and pos > neu:
            return "pos"
        elif neg > pos and neg > neu:
            return "neg"
        else:
            return "neu"
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
