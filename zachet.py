from collections import Counter
import pymorphy2
import math

morph = pymorphy2.MorphAnalyzer()

pattern_punct = "[!@“’«»#$%&/\"(')*+,/:;<=>?^_`{|}~]\""

"""
Чтение текста из файла
"""
with open('input.txt', 'r') as f:
    text = f.readlines()
text = [line[:-1] for line in text]  # Убираем '\n'
text = [line for line in text if len(line) > 0]  # Убираем пустые строки

full_text = [' '.join(text)]  # Объединяем текст в одну строку
all_words = full_text[0].split()  # Каждое слово в отдельной строке
for word in range(len(all_words)):  # Удаляем символы в словах
    for letter in all_words[word]:
        if letter in pattern_punct:
            all_words[word] = all_words[word].replace(letter, '')
all_words = [word for word in all_words if word != '-']  # Удаляем "-"

text_length = len(all_words)  # Кол-во слов в тексте

c = dict(Counter([morph.parse(i)[0].normal_form
         for i in all_words if
         str.isalpha(morph.parse(i)[0].normal_form)]))  # Приводим слова к н.ф.

sub_dict = list(c.items())
sub_dict.sort(key=lambda i: i[1])
sub_dict = sub_dict[::-1]
word_usage = dict(sub_dict)  # Cловарь с кол-вом использований уникальных слов

cl_s = dict()  # cl_s значит "classical sickness"
for i in range(len(word_usage)):  # Словарь с кл.тошнотой каждого слова
    cl_s[list(word_usage.items())[i][0]] = \
        round(math.sqrt(list(word_usage.items())[i][1]), 2)

cl_s_top = list(cl_s.items())[:7]  # 7 самых частых слов
cl_s_top_words = ''
for i in cl_s_top:
    cl_s_top_words += (i[0] + ': ' + str(i[1]) + '\n')

if cl_s_top[0][1] <= 7:  # Результат проверки на кл. тошноту
    cl_s_result = 'Текст не переспамлен\n'
else:
    cl_s_result = 'Текст переспамлен\n'

cl_s_lines = ['КЛАССИЧЕСКАЯ ТОШНОТА\n', cl_s_top_words, cl_s_result]

border = '-------------\n'

ac_s = dict()  # ac_s значит "academic sickness"
auxiliary_pos = ['NPRO', 'PREP', 'CONJ', 'PRCL', 'INTJ']  # служебн. части речи
ac_s_subdict = [i for i in list(word_usage.items()) if  # Удаляем сл.части речи
                morph.parse(i[0])[0].tag.POS not in auxiliary_pos]

all_indep_words = 0  # Найдем кол-во слов самост. частей речи
for i in range(len(ac_s_subdict)):
    all_indep_words += ac_s_subdict[i][1]

for i in range(len(ac_s_subdict)):  # Словарь с ак.тошнотой каждого слова
    ac_s[ac_s_subdict[i][0]] = \
        round(ac_s_subdict[i][1]*100/all_indep_words, 2)

ac_s_top = list(ac_s.items())[:5]  # 5 самых частых слов
ac_s_top_words = ''
for i in ac_s_top:
    ac_s_top_words += (i[0] + ': ' + str(i[1]) + '%\n')

if ac_s_top[0][1] <= 8:  # Результат проверки на ак. тошноту
    ac_s_result = 'Текст не переспамлен\n'
else:
    ac_s_result = 'Текст переспамлен\n'

ac_s_lines = ['АКАДЕМИЧЕСКАЯ ТОШНОТА\n', ac_s_top_words, ac_s_result]

number_of_words = ['Количество слов в тексте: ', str(text_length), '\n',
                   'Кол-во слов самостоятельных частей речи: ',
                   str(all_indep_words)]

with open('output_2.txt', 'w') as f:  # Запись рез-тов в файл
    if text_length < 1500:
        for line in cl_s_lines:
            f.write(line)
        f.write(border)
    for line in ac_s_lines:
        f.write(line)
    f.write(border)
    for line in number_of_words:
        f.write(line)
