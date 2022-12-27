#трансформировать содержимое movies.xml в формат json

import xml.etree.ElementTree as ET
import json

tree = ET.parse('movies.xml')
root = tree.getroot()
dict={}
for child in root:
    if child.tag not in dict:
        dict[child.tag]=[]
    dict2={}
    for child2 in child:
        if child2.tag not in dict2:
            dict2[child2.tag]=child2.text
    dict[child.tag].append(dict2)
#print(d)

with open("data_file.json", "w") as write_file:
    json.dump(dict, write_file)