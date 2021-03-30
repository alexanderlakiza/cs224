import requests
import json
import Levenshtein as lev


def check_spelling(text):
    domain = "https://speller.yandex.net/services/spellservice.json"
    words = text.split()
    if len(words) == 1:
        request = requests.get(domain + "/checkText?text=" + words[0])
        if requests:
            if not request.json():
                for i in range(len(words[0])):
                    if ord(words[0][i]) < 1040:
                        return 'В слове "{}" присутствуют буквы не русского языка'.format(words[0])
                return 'В слове "{}" нет ошибки'.format(words[0])
            else:
                return request.json()[0]["word"], request.json()[0]["s"]
        else:
            return None
    elif len(words) > 1:
        words = "+".join(words)
        request = requests.get(domain + "/checkText?text=" + words)
        if requests:
            if not request.json():
                words = words.split("+")
                for word in words:
                    for i in range(len(word)):
                        if ord(word[i]) < 1040:
                            return 'В слове "{}" присутствуют буквы не русского языка'.format(word)
                return 'В словах {} нет ошибок'.format(words)
            else:
                response = [(i["word"], i["s"]) for i in request.json()]
                return response
        else:
            return None
    return None


def fix_flaw(word):
    # options = check_spelling(word)[1]
    lev_distances = {}
    for i in list(word_usage.keys()):
        lev_distances[i] = lev.distance(word, i)
    """
    Реализация исправления ошибки через Яндекс спелл чекер
    for i in options:
        lev_distances[i] = lev.distance(word, i)
    """
    minimum = list(lev_distances.values()).index(min(list(lev_distances.values())))
    best_option = list(lev_distances.keys())[minimum]
    return best_option


with open("each_token_appearance.json") as f:
    word_usage = json.load(f)


def show(word):
    dict_of_docs = word_usage[word]
    number_of_mentions = list(dict_of_docs.keys())[0]
    print('Слово "{}" встречается {} раз в документах: {}'.format(word, number_of_mentions,
                                        dict_of_docs[number_of_mentions]))

if __name__ == "__main__":
    print('Данная программа покажет вам названия документов, в которых встречается введенное вами слово\n\n'
          'Введите ваше слово в начальной форме: ')
    word = input()
    if word in list(word_usage.keys()):
        show(word)
    else:
        print('Слово "{}" в документах не наблюдается\n'.format(word))
        print('Возможно вы имели в виду слово "{}"\n'.format(fix_flaw(word)))
        fixed_word = fix_flaw(word)
        show(fixed_word)
