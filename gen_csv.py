import csv
import json
from collections import defaultdict
from ngram.ngram import generate_N_grams

with open("data/dict.json", "r") as f:
    merged_d = json.load(f)
    val = {}
    for v in merged_d.values():
        val.update(v)
with open("data/state.json", "r") as f:
    state_code = json.load(f)

def gen_notes_tags_csv():
    note_tags = defaultdict(set)
    with open("raw/3_govt_urls_state_only.csv", "r") as f:
        data = csv.DictReader(f)
        for row in data:
            original_note = row["Note"]
            note = original_note.split("--")[0]
            for i in range(2, 4):
                ngram = generate_N_grams(note.lower(), i)
                for gram in ngram:
                    if gram in val:
                        note_tags[original_note].add(gram)

    with open("data/note_tags.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter = ',',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['states','tags', 'notes'])
        for key, value in note_tags.items():
            s = set()
            for k,k2 in zip(key.split(),generate_N_grams(key.lower(),2)):
                k = k.title()
                k2 = k2.title()
                if k2 in state_code:
                    s.add(k2)
                if k in state_code:
                    s.add(k)
            list_s = list(s)
            if len(list_s) >= 2:
                if list_s[1] in list_s[0]:
                    list_s.pop()
            value = ','.join(value)
            states = ','.join(list_s)
            writer.writerow([states,value, key])

gen_notes_tags_csv()
 

