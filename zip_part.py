import zipfile
import os
import pathlib

def create_and_insert(archive_name,file_name):
    with zipfile.ZipFile(archive_name, "w") as myzip:
        myzip.write(file_name)

def read(archive_name,file_name):
    with zipfile.ZipFile(archive_name, "r") as myzip:
        myzip.extract(file_name)
        with open(file_name, "r") as file:
            print(file.read())


def delete(archive_name,file_name):
    file_path = str(pathlib.Path.cwd()) + "\\" + file_name
    archive_path = str(pathlib.Path.cwd()) + "\\" + archive_name
    if os.path.isfile(file_path):
        os.remove(file_path)
        print("Файл успешно удалён")
    else:
        print("Данного файла не существует")
    if os.path.isfile(archive_path):
        os.remove(archive_path)
        print("Архив успешно удалён")
    else:
        print("Данного архива не существует")

archive_name = input("Введите название архива: ") + ".zip"
file_name = input("Введите название файла: ")
create_and_insert(archive_name,file_name)
read(archive_name,file_name)
delete(archive_name,file_name)