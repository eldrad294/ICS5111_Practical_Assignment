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
    def __get_positive_corpus(self):
        return self.__training_positive_corpus
    #
    def __get_negative_corpus(self):
        return self.__training_negative_corpus
    #
    def __get_neutral_corpus(self):
        return self.__training_neutral_corpus
    #
    def get_test_corpus(self):
        text, classifications = self.__testing_corpus['text'], self.__testing_corpus['classification']
        return text, classifications
    #
    def get_vocab(self):
        """ Our vocab corpus, returns 3 lists (positive,negative,neutral)
            This will need to be replaced with the actual nltk/equivalent word corpus"""
        positive_vocab = tuple(self.__get_positive_corpus()[0])
        negative_vocab = tuple(self.__get_negative_corpus()[0])
        neutral_vocab = tuple(self.__get_neutral_corpus()[0])
        return positive_vocab, negative_vocab, neutral_vocab