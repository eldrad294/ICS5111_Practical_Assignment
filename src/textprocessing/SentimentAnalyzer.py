from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
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
        train_set = self.__train_vocab()
        self.__NBclassifier = self.__train_classifier(train_set)
    #
    def __word_feats(self, words):
        """ Takes a word and converts it into a python dictionary """
        return dict([(word, True) for word in words])
    #
    def __get_vocab(self):
        """ Our vocab corpus, returns 3 lists (positive,negative,neutral)
            This will need to be replaced with the actual nltk/equivalent word corpus"""
        positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)',
                          'underpriced']
        negative_vocab = ['bad', 'terrible', 'useless', 'hate', ':(', 'shit', 'strange', 'threw up', 'vomit',
                          'overpriced']
        neutral_vocab = ['movie', 'the', 'sound', 'was', 'is', 'actors', 'did', 'know', 'words', 'not']
        return positive_vocab, negative_vocab, neutral_vocab
    #
    def __train_vocab(self):
        """ Returns an entire set of vocab which is marked as either 1) Positive, 2) Negative, 3) Neutral """
        positive_vocab, negative_vocab, neutral_vocab = self.__get_vocab()
        positive_features = [(self.__word_feats(pos), 'pos') for pos in positive_vocab]
        negative_features = [(self.__word_feats(neg), 'neg') for neg in negative_vocab]
        neutral_features = [(self.__word_feats(neu), 'neu') for neu in neutral_vocab]
        return positive_features + negative_features + neutral_features
    #
    def __train_classifier(self, train_set):
        """ Takes the training vocab (consisting of pos,neg,neu) vocab and trains itself. """
        return NaiveBayesClassifier.train(train_set)
    #
    def predict(self,sentence):
        """ Public function. Takes a sentence as parameter and assigns a sentiment label to it (pos/neg/neu) """
        pos,neg,neu = 0,0,0
        #
        # Convert into bag of words
        sentence = sentence.lower().split(' ')
        #
        # Remove stop words
        filtered_words = [word for word in sentence if word not in stopwords.words('english')]
        #
        for word in filtered_words:
            prediction = self.__NBclassifier.classify(self.__word_feats(word))
            if prediction == "pos":
                pos += 1
            elif prediction == "neg":
                neg += 1
            elif prediction == "neu":
                neu += 1
        #
        if pos > neg and pos > neu:
            return "pos"
        elif neg > pos and neg > neu:
            return "neg"
        else:
            return "neu"