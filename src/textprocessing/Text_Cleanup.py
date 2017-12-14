import re
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
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