from src.textprocessing.Scoring_Functions import Scoring_Functions
from nltk.corpus import stopwords
from src.textprocessing.Word_Corpus import WordCorpus
from sklearn.metrics import accuracy_score
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag
from nltk import PorterStemmer
from src.textprocessing.Text_Cleanup import TextCleanup
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import numpy as np
#
class SentimentAnalyzer():
    #
    """ An example as to how invoke and use this class:
            from src.textprocessing.SentimentAnalyzer import SentimentAnalyzer
            sa = SentimentAnalyzer()
            pred = sa.predict("I will never go there again")
            print(pred)
    """
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.__word_corpus = WordCorpus()
        X, y = self.__format_vocab()
        self.__LRclassifier = self.__train_classifier(X, y)
        self.text_cleanup = TextCleanup()
    #
    def __format_vocab(self):
        """ Returns an entire set of vocab which is marked as either 1) Positive, 2) Negative, 3) Neutral for NLTK
        classification """
        positive_vocab, negative_vocab, neutral_vocab = self.__word_corpus.get_vocab()
        pos_list, neu_list, neg_list = [],[],[]
        #
        [(pos_list.append('pos')) for i in range(len(positive_vocab))]
        [(neu_list.append('neu')) for i in range(len(neutral_vocab))]
        [(neg_list.append('neg')) for i in range(len(negative_vocab))]
        #
        return positive_vocab + negative_vocab + neutral_vocab, pos_list + neu_list + neg_list
    #
    def __train_classifier(self, X, y=None):
        """ Takes the training vocab (consisting of pos,neg,neu) vocab and trains itself """
        #
        # Logistic Regression Classifier
        X = self.vectorizer.fit_transform(X)
        return LogisticRegression().fit(X,y)
    #
    def __classify(self, word):
        """ Takes input sample and classifies it as either pos / neu / neg """
        #
        # Logistic Regression Classifier
        word = self.vectorizer.fit_transform(word)
        print(word)
        return self.__LRclassifier.predict(word)
    #
    def predict(self,sentence):
        """ Public function. Takes a sentence as parameter and assigns a sentiment label to it (pos/neg/neu) """
        pos,neg,neu = 0,0,0
        #
        filtered_words =self.text_cleanup.clean_sentence(sentence)
        for word in filtered_words:
            prediction = self.__classify(word)
            print(str(word) + " - " + str(prediction))
            if prediction == "pos":
                pos += 1
            elif prediction == "neg":
                neg += 1
            elif prediction == "neu":
                neu += 1
        #
        print('-----------------')
        print(pos)
        print(neu)
        print(neg)
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
        results = []
        test_sentences, expected_results = self.__word_corpus.get_test_corpus()
        #
        [(results.append(self.__LRclassifier.predict(sentence))) for sentence in test_sentences]
        #
        accuracy = Scoring_Functions().accuracy(list(results) ,list(expected_results))
        precision = Scoring_Functions().precision(set(results) ,set(expected_results))
        recall = Scoring_Functions().recall(set(results) ,set(expected_results))
        f_measure = Scoring_Functions().f_measure(set(results) ,set(expected_results))
        return "Accuracy: " + str(accuracy) + "\nPrecision: " + str(precision) + "\nRecall: " + str(recall) + "\nF_Measure: " + str(f_measure)