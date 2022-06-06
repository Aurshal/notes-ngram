import csv
import json
from collections import defaultdict
from ngram.ngram import generate_N_grams


d = defaultdict(list)
d2 = defaultdict(list)
d3 = defaultdict(list)


def func(text: str, n: int, original_text: str):
    global d
    global d2
    global d3
    ngram = (generate_N_grams(text, n))
    for i in ngram:
        i = i.lower()
        if n == 1:
            if d[i]:
                d[i] = [(d[i])[0] + 1, original_text]
            else:
                d[i] = [1, original_text]

        elif n == 2:
            if d2[i]:
                d2[i] = [(d2[i])[0] + 1, original_text]
            else:
                d2[i] = [1, original_text]
        else:
            if d3[i]:
                d3[i] = [(d3[i])[0] + 1, original_text]
            else:
                d3[i] = [1, original_text]


with open('raw/3_govt_urls_state_only.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        original_note = row['Note']
        index = 0
        for ind, s in enumerate(original_note):
            if s == '-':
                index = ind
                break
        note = original_note[0:index]
        for i in range(1, 4):
            func(note, i, original_note)
s_d = (sorted(d.items(), key=lambda item: item[1][0], reverse=True))[:30]
s_d2 = sorted(d2.items(), key=lambda item: item[1][0], reverse=True)[:30]
s_d3 = sorted(d3.items(), key=lambda item: item[1][0], reverse=True)[:30]
dic = {
    "unigram": dict(s_d),
    "bigram": dict(s_d2),
    "trigram": dict(s_d3),
}
with open('data/dict.json', 'w') as f:
    json.dump(dic, f, indent=4)
