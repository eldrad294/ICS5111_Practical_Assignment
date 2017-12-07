import pandas as pd
#
class WordCorpus():
    #
    def __init__(self):
        self.__positive_corpus = pd.read_csv('../data/Positive_Corpus.csv', header=None, encoding = "ISO-8859-1")
        self.__negative_corpus = pd.read_csv('../data/Negative_Corpus.csv', header=None, encoding = "ISO-8859-1")
        self.__neutral_corpus = pd.read_csv('../data/Neutral_corpus.csv', header=None, encoding = "ISO-8859-1")
    #
    def get_positive_corpus(self):
        return self.__positive_corpus
    #
    def get_negative_corpus(self):
        return self.__negative_corpus
    #
    def get_neutral_corpus(self):
        return self.__neutral_corpus