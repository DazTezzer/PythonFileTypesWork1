import json
import os
import pathlib


class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getCountry(self):
        return self.country


def create(file_name):
    with open(file_name, "w") as file:
        json.dump([], file)


def insert(file_name, json_data):
    with open(file_name, "w") as file:
        json.dump(json_data, file)


def read(file_name):
    with open(file_name, "r") as file:
        print(file.read())


def delete(file_name):
    path = str(pathlib.Path.cwd()) + "\\" + file_name
    if os.path.isfile(path):
        os.remove(path)
        print("Успешно удалён")
    else:
        print("Данного файла не существует")


file_name = input("Введите название файла: ") + ".json"
person = Person(input("Имя "), input("Возраст "), input("Страна "))
json_data = {"name": person.getName(), "age": person.getAge(), "country": person.getCountry()}
create(file_name)
insert(file_name, json_data)
read(file_name)
delete(file_name)
