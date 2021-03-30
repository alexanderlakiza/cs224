import wikipediaapi as wikiapi
import time
import json


wiki = wikiapi.Wikipedia("ru")
page = wiki.page("Титаник")  # Будем брать данные со страницы Титаника

links = page.links
ru_links = [i for i in sorted(list(links.keys())) if ord(i[0]) >= 1040
            and ord(i[-1]) >= 1040]
ru_links = [i for i in ru_links if ':' not in i]
ru_links = [i for i in ru_links if ',' not in i]
# Оставляем лишь ссылки на русском
# Удаляем ссылки, в которых есть скобки и запятые

data = {}

for i in ru_links:
    page = wiki.page(i)
    if page.exists():
        data[i] = page.summary
    time.sleep(1)
    print(i, 'is done')
# Заполянем наш словарь

data['corpus_length'] = len(data)
# Добавляем информацию о кол-ве заголовков

with open("titanic_data.json", "w") as f:
    # Записываем наш корпус в формате .json
    json.dump(data, f, ensure_ascii=False)
