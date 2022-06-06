import csv
import json
from ngram.ngram import generate_N_grams

with open('data/dict.json', 'r') as f:
    d = json.load(f)

merged_d = {**d['unigram'], **d['bigram'], **d['trigram']}


def get_notes(text):
    global merged_d
    text = text.lower()
    unigram = generate_N_grams(text, 1)
    bigram = generate_N_grams(text, 2)
    trigram = generate_N_grams(text, 3)
    merged = [*unigram, *bigram, *trigram]
    notes = []
    for i in merged:
        try:
            note = merged_d[i][1]
            if notes and note in notes:
                continue
            else:
                notes.append(note)
                return note
        except:
            continue


print(get_notes('public commission'))
