# Получают все ссылки ведующие на wikipedia c любой из страниц википедии 
# с помощью библиотеки httpx (либо requests, либо стандартной urllib.request) 
# и языка запросов xpath для обработки xml-подобных данных 
import wikipediaapi
import socket
wiki = wikipediaapi.Wikipedia("en")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = 'ru.wikipedia.org'
    port = 80
    s.connect((host, port))

def all_page_links(page) -> list:
    list = []
    links = page.links
    for link in links:
        if wiki.page(link):
            list.append(link)
    return list

page = wiki.page('Strawberry_pie')
print(all_page_links(page))