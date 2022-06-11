import string
from nltk.corpus import stopwords
manual_symbols = ['।']
symbols = string.punctuation + ''.join(manual_symbols)


def remove_punctuation(text:str)->str:
    if isinstance(text, float):
        return str(text)
    new_text = ""
    for i in text:
        if i not in symbols:
            new_text += i
    return new_text


def generate_N_grams(text:str, ngram=1):
    text = remove_punctuation(text)
    sw = (stopwords.words("english"))
    words = [
        word for word in text.split() if word != '']
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans = [" ".join(ngram) for ngram in temp]
    return ans
