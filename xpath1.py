# вывести на экран словарь, ключи которого - 
# названия фильмов, значения - содержимое "runtime"

import xml.etree.ElementTree as ET 

tree = ET.parse('movies.xml')  
root = tree.getroot() 
dict = {}
for Title in root.iter('Title'):
    time = Title.attrib.get('runtime')
    name = Title.text
    dict[name] = time
print(dict)