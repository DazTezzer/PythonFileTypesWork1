import os
import pathlib


def create(file_name):
    f = open(file_name, "w")
    f.close()


def insert(file_name):
    f = open(file_name, "w")
    f.write(input("Введите текст : "))
    f.close()


def read(file_name):
    f = open(file_name, "r")
    print(f.read())
    f.close()


def delete(file_name):
    path = str(pathlib.Path.cwd()) + "\\" + file_name
    if os.path.isfile(path):
        os.remove(path)
        print("Успешно удалён")
    else:
        print("Данного файла не существует")


file_name = input("Введите название файла: ") + ".txt"
create(file_name)
insert(file_name)
read(file_name)
delete(file_name)
