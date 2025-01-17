import operator
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
import re
#
class Word_Bucket():
    #
    def __init__(self):
        pass
    #
    def get_top_N_frequent_words(self, text, N=10, pos=False):
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
        i = 0
        for x in range(len(frequency_words)):
            if i > N:
                break
            if pos==True:
                tagged_sentence = pos_tag(word_tokenize(frequency_words[x][0]))
                stripped_tags = ['VB','VBG','VBN','VBP','VBZ','WP','JJ','JJR','JJS','FW','WRB', 'RB','RBR','RBS','RP','UH','CC'] # https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/
                for word, type in tagged_sentence:
                    if type in stripped_tags:
                        keys.append(frequency_words[x][0])
                        values.append(frequency_words[x][1])
                        i += 1
            else:
                keys.append(frequency_words[x][0])
                values.append(frequency_words[x][1])
                i += 1
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
        punctuation = ('.',',',':',';','"','\'','!','?','+','-','{','}','(',')','[',']','#','&','$','/','*','%','^','@','=', '\n', '\r', '\t','')
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
