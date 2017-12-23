import re
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, SnowballStemmer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.util import ngrams
from nltk.stem import WordNetLemmatizer
#
class TextCleanup():
    #
    def __init__(self):
        pass
    #
    def clean_sentence(self,sentence):
        """ Takes input sentence, and formats it in a presentable state for the classifier """
        #
        # Remove numerics
        sentence = re.sub(r'\d+', '', sentence)
        #
        # Convert to lowercase
        sentence = sentence.lower()
        #
        # Tokenize (split into unigrams) for sentence cleanup
        sentence = self.__word_grams(sentence,1)
        #
        # Remove stop words
        filtered_words = [word for word in sentence if word not in stopwords.words('english')]
        #
        # Sentence Tagging & Removal
        tagged_sentence = pos_tag(filtered_words)
        stripped_tags = ['NN','NNS','NNP','NNPS','CD','UH'] # https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/
        filtered_words = [word for word,type in tagged_sentence if type not in stripped_tags]
        #
        # Perform Stemming
        #stemmer = PorterStemmer()
        #stemmer = SnowballStemmer('english')
        #filtered_words = [(stemmer.stem(word)) for word in filtered_words]
        #
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        filtered_words = [(lemmatizer.lemmatize(word)) for word in filtered_words]
        #
        # Split into n-grams
        filtered_words = self.__word_grams(" ".join(filtered_words), 3)
        #print(filtered_words)
        #print(tagged_sentence)
        return filtered_words
    #
    def __word_grams(self, sentence, N=1):
        s = []
        tokenizer = RegexpTokenizer(r'\w+')
        sentence = tokenizer.tokenize(sentence)
        for ngram in ngrams(sentence, N):
            s.append(' '.join(str(i) for i in ngram))
        return s