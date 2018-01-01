from nltk.classify import NaiveBayesClassifier
from nltk import precision
from sklearn.naive_bayes import MultinomialNB
from src.textprocessing.Word_Corpus import WordCorpus
from src.textprocessing.Text_Cleanup import TextCleanup
from src.textprocessing.Scoring_Functions import Scoring_Functions
from sklearn.feature_extraction.text import TfidfVectorizer
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
        self.vectorizer = TfidfVectorizer()
        self.__word_corpus = WordCorpus()
        X, y = self.__format_vocab()
        self.__NBclassifier = self.__train_classifier(X, y)
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
        # Scikit Naive Bayes Multinomial classifier.
        X = self.vectorizer.fit_transform(X)
        print(self.vectorizer)
        classifier = MultinomialNB().fit(X,y)
        print(classifier)
        return classifier
    #
    def __classify(self, word):
        """ Takes input sample and classifies it as either pos / neu / neg """
        #
        # Scikit Naive Bayes Multinomial classifier.
        word = self.vectorizer.transform([word])
        return self.__NBclassifier.predict(word)
    #
    def predict(self,sentence):
        """ Public function. Takes a sentence as parameter and assigns a sentiment label to it (pos/neg/neu) """
        pos,neg,neu = 0,0,0
        neutral_weight = 0  # We introduce a weight to positive and negative scalar counts, to classify as neutral in the case of close pos-neg tie ins
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
        if pos-neutral_weight > neg and pos-neutral_weight > neu:
            return "pos"
        elif neg-neutral_weight > pos and neg-neutral_weight > neu:
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
