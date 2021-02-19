import wikipediaapi as wikiapi
import time


wiki = wikiapi.Wikipedia("ru")
page = wiki.page("Титаник")
if page.exists():
    print(page.summary, sep="\n")

links = page.links
ru_links = [i for i in sorted(list(links.keys())) if ord(i[0]) >= 1040 and ord(i[-1]) >= 1040]
ru_links = [i for i in ru_links if not ':' in i]
ru_links = [i for i in ru_links if not ',' in i]
for i in ru_links:
    page = wiki.page(i)
    time.sleep(1)
    if page.exists():
        print(page.summary, sep="\n")

