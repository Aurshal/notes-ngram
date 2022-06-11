import csv
import json
from collections import defaultdict
from ngram.ngram import generate_N_grams
from nltk.corpus import stopwords


sw = (stopwords.words("english"))
def sort_by_value(d):
    sorted_d = (sorted(d.items(), key=lambda item: item[1], reverse=True))[:20]
    return dict(sorted_d)


with open("raw/3_govt_urls_state_only.csv", "r") as f:
    general_dict = defaultdict(dict)
    data = csv.DictReader(f)
    for row in data:
        original_note = row["Note"]
        note = original_note.split("--")[0]
        for i in range(2, 4):
            ngram = generate_N_grams(note.lower(), i)
            for gram in ngram:
                split_gram = gram.split()
                if (split_gram[0] in sw) or (split_gram[-1] in sw):
                    continue
                else:
                    try:
                        general_dict[i][gram]+=1
                    except KeyError:
                        general_dict[i][gram]=1

for k,v in general_dict.items():
    updated_v = sort_by_value(v)
    general_dict[k] = updated_v
with open("data/dict.json", "w") as f:
    json.dump(general_dict, f, indent=4, ensure_ascii=False)

