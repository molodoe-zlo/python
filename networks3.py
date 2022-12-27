# Выдает сколько и какие переходы в wikipedia нужно совершить между двумя страницами этого сервиса, 
# например https://ru.wikipedia.org/wiki/Философия и https://ru.wikipedia.org/wiki/Математика)
# можно использовать либо разбор html-кода с помощью xpath или 
# API сервиса https://wikipedia-api.readthedocs.io/en/latest/README.html
import wikipediaapi
import socket
wiki = wikipediaapi.Wikipedia("ru")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = 'ru.wikipedia.org'
    port = 80
    s.connect((host, port))

def get_page_path(paths, page_to_find, page_to_stop) -> list:
    now = page_to_find
    path = [now]
    while now != page_to_stop:
        now = paths[now]
        path.append(now)
    return path

def findpath(from_page, to_page) -> dict:
    dict = {}
    dict[from_page] = 0
    came_from = {from_page: None}
    path = [from_page]
    while path:
        now = path.pop(0)
        links_dict = now.links
        for neighbor in links_dict:
            if links_dict[neighbor] not in dict:
                dict[links_dict[neighbor]] = dict[now] + 1
                path.append(links_dict[neighbor])
                came_from[links_dict[neighbor]] = now
            if neighbor == to_page.title:
                return [dict[links_dict[neighbor]], get_page_path(came_from, links_dict[neighbor], from_page)]

def print_anser(pages) -> None:
    page_from = pages[1][0].title
    page_to = pages[1][-1].title
    print("Кратчайший путь от ", page_from, "до", page_to, "= ", pages[0])
    print(end="")
    for i in pages[1]:
        title = i.title
        if title == page_to:
            print(title)
        else:
            print(title, "<- ", end="")


page_from = wiki.page('Философия')
page_to = wiki.page('Математика')
path = findpath(page_from, page_to)
print_anser(path)