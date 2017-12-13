from nltk.classify import NaiveBayesClassifier
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from src.textprocessing.Word_Corpus import WordCorpus
from sklearn.metrics import accuracy_score
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag
from nltk import PorterStemmer
from nltk import ngrams
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
        self.__word_corpus = WordCorpus()
        #train_set = self.__format_vocab_NLTK()
        train_set, train_labels = self.__format_vocab_GaussianNB()
        #self.__NBclassifier = self.__train_classifier(train_set)
        self.__NBclassifier = self.__train_classifier(train_set, train_labels)
    #
    def __word_feats(self, words):
        """ Takes a word and converts it into a python dictionary """
        return dict([(words.lower(), True)])
    #
    def __get_vocab(self):
        """ Our vocab corpus, returns 3 lists (positive,negative,neutral)
            This will need to be replaced with the actual nltk/equivalent word corpus"""
        # positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)',
        #                   'underpriced']
        # negative_vocab = ['bad', 'terrible', 'useless', 'hate', ':(', 'shit', 'strange', 'threw up', 'vomit',
        #                   'overpriced', 'despicable', 'late', 'delayed', 'cancelled']
        # neutral_vocab = ['movie', 'the', 'sound', 'was', 'is', 'actors', 'did', 'know', 'words', 'not']
        positive_vocab = tuple(self.__word_corpus.get_positive_corpus()[0])
        negative_vocab = tuple(self.__word_corpus.get_negative_corpus()[0])
        neutral_vocab = tuple(self.__word_corpus.get_neutral_corpus()[0])
        return positive_vocab, negative_vocab, neutral_vocab
    #
    def __format_vocab_NLTK(self):
        """ Returns an entire set of vocab which is marked as either 1) Positive, 2) Negative, 3) Neutral for NLTK
        classification """
        positive_vocab, negative_vocab, neutral_vocab = self.__get_vocab()
        #
        positive_features = [(self.__word_feats(str(pos)), 'pos') for pos in positive_vocab]
        negative_features = [(self.__word_feats(str(neg)), 'neg') for neg in negative_vocab]
        neutral_features = [(self.__word_feats(str(neu)), 'neu') for neu in neutral_vocab]
        #
        return positive_features + negative_features + neutral_features
    #
    def __format_vocab_GaussianNB(self):
        """ Returns an entire set of vocab which is marked as either 1) Positive, 2) Negative, 3) Neutral for Scikit
        GaussianNB classification """
        positive_vocab, negative_vocab, neutral_vocab = self.__get_vocab()
        #
        pos_list, neu_list, neg_list = [],[],[]
        [(pos_list.append(0)) for i in range(len(positive_vocab))]
        [(neu_list.append(1)) for i in range(len(neutral_vocab))]
        [(neg_list.append(2)) for i in range(len(negative_vocab))]
        #
        return positive_vocab + neutral_vocab + negative_vocab, pos_list + neu_list + neg_list
    #
    def __train_classifier(self, train_set, train_labels=None):
        """ Takes the training vocab (consisting of pos,neg,neu) vocab and trains itself """
        #
        # NLTK's Naive Bayes classifier.
        #return NaiveBayesClassifier.train(train_set)
        #
        # Scikit's Gaussian Naive Bayes
        train_set = np.array(train_set).reshape(-1,1)
        return MultinomialNB().fit(train_set,train_labels)
    #
    def __classify(self, word):
        """ Takes input sample and classifies it as either pos / neu / neg """
        #
        # NLTK Naive Bayes Classification
        # Convert word into dictionary to be classified by the classifier
        #return self.__NBclassifier.classify(self.__word_feats(word))
        # Scikit Gaussian Naive Bayes Classification
        return self.__NBclassifier.predict(word)
    #
    def predict(self,sentence):
        """ Public function. Takes a sentence as parameter and assigns a sentiment label to it (pos/neg/neu) """
        pos,neg,neu = 0,0,0
        #
        filtered_words = self.__clean_sentence(sentence)
        #self.__NBclassifier.show_most_informative_features()
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
    def __clean_sentence(self,sentence):
        """ Takes input sentence, and formats it in a presentable state for the classifier """
        #
        # Remove numerics
        sentence = re.sub(r'\d+', '', sentence)
        #
        # Remove punctuation
        tokenizer = RegexpTokenizer(r'\w+')
        sentence = tokenizer.tokenize((sentence.lower()))
        #
        # Remove stop words
        filtered_words = [word for word in sentence if word not in stopwords.words('english')]
        #
        # Perform Stemming
        stemmer = PorterStemmer()
        filtered_words = [(stemmer.stem(word)) for word in filtered_words]
        #
        # Noun Tagging & Removal
        tagged_sentence = pos_tag(filtered_words)
        stripped_tags = ['NN','NNS','NNP','CD'] # https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
        filtered_words = [word for word,type in tagged_sentence if type not in stripped_tags]
        #
        return filtered_words
    #
    def accuracy(self):
        """ Public function. Uses the classifier on the testing set of data to determine the accuracy """
        #
        results = []
        test_sentences, expected_results = self.__word_corpus.get_test_corpus()
        #
        for sentence in test_sentences:
            results.append(self.__NBclassifier.classify(self.__word_feats(sentence)))
        #
        return str(accuracy_score(expected_results,results) * 100) + '%'