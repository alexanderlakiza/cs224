import json
import pymorphy2
import pandas as pd


morph = pymorphy2.MorphAnalyzer()


with open("corpus_as_dict_of_norms.json") as f:
    normed_dict = json.load(f)


"""
normed_dict_with_pos = {}
for title in list(normed_dict.keys()):
    normed_dict_with_pos[title] = [(word, morph.parse(word)[0].tag.POS) for word in normed_dict[title]
                                   if morph.parse(word)[0].tag.POS is not None]


with open("corpus_as_dict_of_norms_and_pos.json", "w") as f:
    # Запишем корпус в виде словаря в json, чтобы потом использовать готовый словарь
    # вместо использования pymorphy2
    json.dump(normed_dict_with_pos, f, ensure_ascii=False)
"""


with open("corpus_as_dict_of_norms_and_pos.json") as f:
    corpus_tokens_pos = json.load(f)


for title in list(corpus_tokens_pos.keys()):
    for word in list(corpus_tokens_pos[title]):
        if word[1] == 'ADJF':
            word[1] = 'ADJ'
        elif word[1] == 'ADJS':
            word[1] = 'ADJ'
        elif word[1] == 'COMP':
            word[1] = 'ADJ'
        elif word[1] == 'INFN':
            word[1] = 'VERB'
        else:
            pass

# print(corpus_tokens_pos)

corpus_pos_ratios = {}
for title in list(corpus_tokens_pos.keys()):
    value = corpus_tokens_pos[title]
    poses_of_doc = [token[1] for token in value]
    doc_poses_ratios = [[pos, round(poses_of_doc.count(pos)/len(poses_of_doc), 3)]
                        for pos in set(poses_of_doc)]
    corpus_pos_ratios[title] = doc_poses_ratios


lengths_pos = list(map(len, list(corpus_pos_ratios.values())))
index_max_n_pos = lengths_pos.index(max(lengths_pos))
used_pos = list(corpus_pos_ratios.values())[index_max_n_pos]
used_pos = [i[0] for i in used_pos]


sorted_c_pos_ratios = {}
for title in list(corpus_pos_ratios.keys()):
    subdict = {}
    for pos in used_pos:
        subdict[pos] = 0
    sorted_c_pos_ratios[title] = subdict

    for pos_ratio in corpus_pos_ratios[title]:
        subdict[pos_ratio[0]] = pos_ratio[1]
print(sorted_c_pos_ratios)


df = pd.DataFrame.from_dict(sorted_c_pos_ratios, orient='index')
print(df)
df.to_csv("pos_ratios.csv")
data = pd.read_csv('pos_ratios.csv')
print(data.head())
