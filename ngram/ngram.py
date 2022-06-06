import string
import nltk
from nltk.corpus import stopwords
manual_symbols = ['।']
symbols = string.punctuation + ''.join(manual_symbols)
symbols = symbols.replace('.', '')


def remove_punctuation(text):
    if isinstance(text, float):
        return text
    new_text = ""
    for i in text:
        if i not in symbols:
            new_text += i
    return new_text


def generate_N_grams(text, ngram=1):
    text = remove_punctuation(text)
    sw = (stopwords.words("english")+stopwords.words("nepali"))
    if ngram == 1:
        sw = sw+['the']
        sw = set(sw)
        words = [
            word for word in text.split(" ") if word != '' and word not in sw]
    else:
        words = [
            word for word in text.split(" ") if word != '']
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans = [" ".join(ngram) for ngram in temp]
    return ans
