import csv
import json
from collections import defaultdict
from ngram.ngram import generate_N_grams


with open('raw/3_govt_urls_state_only.csv', 'r') as f:
    general_dict = defaultdict(list)
    data = csv.DictReader(f)
    for row in data:
        original_note = row['Note']
        index = 0
        note = original_note.split('--')[0]
        for i in range(1, 4):
            ngram = (generate_N_grams(note, i))
            for gram in ngram:
                general_dict[gram.lower()].append(original_note)
    sorted_d = dict(sorted(general_dict.items(),
                           key=lambda item: len(item[1]), reverse=True))


with open('data/dict2.json', 'w') as f:
    json.dump(sorted_d, f, indent=4, ensure_ascii=False)

# d = defaultdict(list)
# d2 = defaultdict(list)
# d3 = defaultdict(list)


# def func(text: str, n: int, original_text: str):
#     global d
#     global d2
#     global d3
#     ngram = (generate_N_grams(text, n))
#     for i in ngram:
#         i = i.lower()
#         if n == 1:
#             if d[i]:
#                 d[i][0] = (d[i])[0] + 1
#                 d[i].append(original_text)
#             else:
#                 d[i] = [1, original_text]

#         elif n == 2:
#             if d2[i]:
#                 d2[i][0] = (d2[i])[0] + 1
#                 d2[i].append(original_text)
#             else:
#                 d2[i] = [1, original_text]
#         else:
#             if d3[i]:
#                 d3[i][0] = (d3[i])[0] + 1
#                 d3[i].append(original_text)
#             else:
#                 d3[i] = [1, original_text]

# def sort_dict_by_value(d, n=20):
#     s_d = (sorted(d.items(), key=lambda item: item[1][0], reverse=True))[:n]
#     return dict(s_d)


# s_d = sort_dict_by_value(d)
# s_d2 = sort_dict_by_value(d2)
# s_d3 = sort_dict_by_value(d3)
# dic = {
#     "unigram": s_d,
#     "bigram": s_d2,
#     "trigram": s_d3,
# }
