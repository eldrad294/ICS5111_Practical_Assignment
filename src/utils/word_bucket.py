import operator
from nltk.corpus import stopwords
import re
#
class Word_Bucket():
    #
    def __init__(self):
        pass
    #
    def get_top_N_frequent_words(self, text, N=10):
        """ Returns top N frequently used words in passed text. """
        #
        text_list = self.__clean_words(text)
        #
        frequency_words = dict()
        for item in text_list:
            if item in frequency_words:
                frequency_words[item] += 1
            else:
                frequency_words[item] = 1
        #
        # Sorting in frequency descending order
        frequency_words = sorted(frequency_words.items(), key=operator.itemgetter(1), reverse=True)
        #
        keys, values = [], []
        for i in range(len(frequency_words)):
            if i >= N:
                break
            keys.append(frequency_words[i][0])
            values.append(frequency_words[i][1])
        #
        return keys, values
    #
    def __clean_words(self, text):
        """ Takes the input text, removes stop words, punctuation """
        #
        text = text.lower()
        #
        # Remove stop words
        pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
        text = pattern.sub('', text)
        #
        # Remove numerics
        text = re.sub(r'\d+', '', text)
        #
        # Remove punctuation
        punctuation = ('.',',',':',';','"','\'','!','?','+','-','{','}','(',')','[',']','#','&','$','/','*','%','^','@','=','/', '\n', '\r', '\t')
        for punct in punctuation:
            text = text.replace(punct,'')
        #
        # Split sentence into separate words into a list, by whitespace delimeter
        text_list = text.split()
        #
        # Remove words with less than 3 characters
        cleaned_text_list = []
        for word in text_list:
            if len(word) > 3:
                cleaned_text_list.append(word)
        #
        return cleaned_text_list
