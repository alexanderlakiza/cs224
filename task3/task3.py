import re
import json
import pymorphy2
import string
import requests

from nltk import word_tokenize

morph = pymorphy2.MorphAnalyzer()

with open("titanic_data.json") as f:
    init_dict = json.load(f)

titles = list(init_dict.keys())[:-1]
texts = list(init_dict.values())[:-1]

""" Очистка текста """


def del_diacritics(text):
    """Фунцкия удаления диакритических знаков"""
    text = re.sub(r'Ё', 'Е', text)
    text = re.sub(r'ё', 'е', text)

    text = re.sub(r'а́', 'а', text)
    text = re.sub(r'А́', 'А', text)

    text = re.sub(r'е́', 'е', text)
    text = re.sub(r'É', 'Е', text)

    text = re.sub(r'и́', 'и', text)
    text = re.sub(r'И́', 'И', text)

    text = re.sub(r'о́', 'о', text)
    text = re.sub(r'О́', 'О', text)

    text = re.sub(r'у́', 'у', text)
    text = re.sub(r'У́', 'У', text)

    text = re.sub(r'ы́', 'ы', text)
    text = re.sub(r'Ы́', 'Ы', text)

    text = re.sub(r'я́', 'я', text)
    text = re.sub(r'Я́', 'Я', text)

    text = re.sub(r'ю́', 'ю', text)
    text = re.sub(r'Ю́', 'Ю', text)

    text = re.sub(r'э́', 'э', text)
    text = re.sub(r'Э́', 'Э', text)
    return text


for i in range(len(texts)):
    texts[i] = re.sub(r'\n', ' ', texts[i])  # Удаление символа переноса строки

    while len(re.findall(r'\([^()]*\)', texts[i])) != 0:  # Удаление скобок и пробелов
        texts[i] = re.sub(r'\([^()]*\)', '', texts[i])
        texts[i] = re.sub(r'\s+(?=(?:[,.?!:;…]))', '', texts[i])
        texts[i] = re.sub(r'\s+', ' ', texts[i])
    # Заменяем диакритические знаки
    texts[i] = del_diacritics(texts[i])

main_dict = dict(zip(titles, texts))
with open("corpus_as_dict.json", "w") as f:
    # Запишем корпус в виде словарь в json
    json.dump(main_dict, f, ensure_ascii=False)

with open("corpus.json") as f:  # Подгружаем корпус
    corpus = json.load(f)
    while len(re.findall(r'\([^()]*\)', corpus)) != 0:
        corpus = re.sub(r'\([^()]*\)', '', corpus)
        corpus = re.sub(r'\s+(?=(?:[,.?!:;…]))', '', corpus)
        corpus = re.sub(r'\s+', ' ', corpus)
    del_diacritics(corpus)


def del_punct(tokens_list):
    punct = string.punctuation + "—" + "«" + "»"
    return [token.lower() for token in tokens_list if token not in punct]



tokens = word_tokenize(corpus)
tokens = del_punct(tokens)

normed_tokens = [morph.parse(i)[0].normal_form for i in tokens  # Список начальных форм всех токенов
                 if str.isalpha(morph.parse(i)[0].normal_form)]
# print(normed_tokens)
unique_norm_tokens = list(set(normed_tokens))

with open("unique_norms_in_corpus.json", "w") as f:
    # Запишем корпус в виде словаря в json, чтобы потом использовать готовый словарь
    # вместо использования pymorphy2
    json.dump(unique_norm_tokens, f, ensure_ascii=False)



"""
main_normed_dict = {}
md_keys = list(main_dict.keys())
md_values = list(main_dict.values())
for i in range(len(main_dict)):
    tokened_value = md_values[i]
    tokened_value = word_tokenize(tokened_value)
    tokened_value = del_punct(tokened_value)
    normed_tokens = [morph.parse(i)[0].normal_form for i in tokened_value
                     if str.isalpha(morph.parse(i)[0].normal_form)]
    main_normed_dict[md_keys[i]] = normed_tokens

with open("corpus_as_dict_of_norms.json", "w") as f:
    # Запишем корпус в виде словаря в json, чтобы потом использовать готовый словарь
    # вместо использования pymorphy2
    json.dump(main_normed_dict, f, ensure_ascii=False)
"""


with open("unique_norms_in_corpus.json") as f:
    unique_norm_tokens = json.load(f)

with open("corpus_as_dict_of_norms.json") as f:
    main_normed_dict = json.load(f)

# print(unique_norm_tokens)

"""
word_usage = {}
for word in unique_norm_tokens:
    counter = 0
    docs_include_word = {}
    list_docs_include_word = []
    for i in range(len(main_normed_dict)):
        if word in list(main_normed_dict.values())[i]:
            # print('Номер документа:', i)
            c = list(main_normed_dict.values())[i].count(word)
            counter += c
            list_docs_include_word.append(list(main_normed_dict.keys())[i])
    docs_include_word[counter] = list_docs_include_word
    word_usage[word] = docs_include_word

with open("each_token_appearance.json", "w") as f:
    # Запишем корпус в виде словаря в json, чтобы потом использовать готовый словарь
    json.dump(word_usage, f, ensure_ascii=False)
"""

with open("each_token_appearance.json") as f:
    word_usage = json.load(f)

print(word_usage)
