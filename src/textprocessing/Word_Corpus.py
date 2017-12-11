import pandas as pd
#
class WordCorpus():
    #
    def __init__(self):
        self.__training_positive_corpus = pd.read_csv('../data/Active Data/Train/Positive_Corpus.csv', header=None,
                                                      encoding = "ISO-8859-1")
        self.__training_negative_corpus = pd.read_csv('../data/Active Data/Train/Negative_Corpus.csv', header=None,
                                                      encoding = "ISO-8859-1")
        self.__training_neutral_corpus = pd.read_csv('../data/Active Data/Train/Neutral_corpus.csv', header=None,
                                                     encoding = "ISO-8859-1")
        self.__testing_corpus = pd.read_csv('../data/Active Data/Test/Test_Corpus.csv')
    #
    def get_positive_corpus(self):
        return self.__training_positive_corpus
    #
    def get_negative_corpus(self):
        return self.__training_negative_corpus
    #
    def get_neutral_corpus(self):
        return self.__training_neutral_corpus
    #
    def get_test_corpus(self):
        text, classifications = self.__testing_corpus['text'], self.__testing_corpus['classification']
        return text, classifications