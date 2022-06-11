import csv
import json
from collections import defaultdict
from ngram.ngram import generate_N_grams

with open("data/dict.json", "r") as f:
    merged_d = json.load(f)
    val = {}
    for v in merged_d.values():
        val.update(v)
print(len(val))
print(val)
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
        writer.writerow(['notes', 'tags'])
        for key, value in note_tags.items():
            value = ','.join(value)
            writer.writerow([value, key])

gen_notes_tags_csv()
 

# def get_notes(text):
#     global merged_d
#     text = text.lower()
#     bigram = generate_N_grams(text, 2)
#     trigram = generate_N_grams(text, 3)
#     merged = [*bigram, *trigram]
#     notes = []
#     for i in merged:
#         try:
#             note = merged_d[i]
#             if notes and note in notes:
#                 continue
#             else:
#                 notes.append(note)
#         except:
#             continue
#     return notes


