import re
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, SnowballStemmer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.util import ngrams
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
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
        # Remove quotes
        sentence = sentence.replace("\"", "")
        #
        # Convert to lowercase
        sentence = sentence.lower()
        #
        # Puts emphasis on first sentence in review
        sentence = str(self._get_first_sentence(sentence,4)) + ' ' + sentence
        #
        # Tokenize (split into unigrams) for sentence cleanup
        sentence = self.__word_grams(sentence,1)
        #
        # Replace negations with antonyms
        #sentence = self.replace_negations(sentence)
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
    def _get_first_sentence(self, sentence, n=0):
        """ Multiplies the first sentence by n times to put more emphasis on the first sentence """
        punctuation_list = ['.','!',':']
        split_sentence = sentence.split(' ')
        exit_flag = False
        #
        # Checks for sentences without punctuation
        for punctuation in punctuation_list:
            if punctuation in sentence:
                exit_flag = True
                break
        #
        if exit_flag is False:
            return " ".join(split_sentence[:10])
        #
        for i in range(len(split_sentence)):
            for punctuation in punctuation_list:
                if punctuation in split_sentence[i]:
                    first_sentence = ""
                    for j in range(n):
                        first_sentence += " ".join(split_sentence[:i+1])
                    return first_sentence

    #
    def __word_grams(self, sentence, N=1):
        s = []
        tokenizer = RegexpTokenizer(r'\w+')
        sentence = tokenizer.tokenize(sentence)
        for ngram in ngrams(sentence, N):
            s.append(' '.join(str(i) for i in ngram))
        return s
    #
    def replace(self, word, pos=None):
        antonyms = set()
        for syn in wordnet.synsets(word, pos=pos):
            for lemma in syn.lemmas():
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())
        if len(antonyms) == 1:
            return antonyms.pop()
        else:
            return None
    #
    def replace_negations(self, sentence):
        i, l = 0, len(sentence)
        words = []
        while i < l:
            word = sentence[i]
            if word == 'not' and i+1 < l:
                ant = self.replace(sentence[i+1])
                if ant:
                    words.append(ant)
                    i+=2
                    continue
            words.append(word)
            i += 1
        return ' '.join(words)