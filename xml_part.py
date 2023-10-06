import xml.etree.ElementTree as ET
import os
import pathlib
def create(file_name):
    root = ET.Element("root")
    tree = ET.ElementTree(root)
    tree.write(file_name)


def insert(file_name, xml_data):
    root = ET.Element("root")
    tree = ET.ElementTree(root)

    data = ET.SubElement(root, "data")
    data.text = xml_data
    tree.write(file_name)

def read(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    for data in root:
        print(data.tag, data.text)


def delete(file_name):
    path = str(pathlib.Path.cwd()) + "\\" + file_name
    if os.path.isfile(path):
        os.remove(path)
        print("Успешно удалён")
    else:
        print("Данного файла не существует")


file_name = input("Введите название файла: ") + ".xml"
json_data = input("Введите данные: ")
create(file_name)
insert(file_name, json_data)
read(file_name)
delete(file_name)