__author__ = 'Ушаков Михаил Викторович'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

print("Путь - ", sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdirs - создание директорий dir_1 - dir_9")
    print("del_dirs - удаление директорий dir_1 - dir_9")
    print("path_info - Показать папки текущей директории")
    print("copy_file - Создать копию файла")

def make_dirs():
    try:
        for dir in range(1, 10):
            os.mkdir(f"dir_{dir}")
            print(f"Директория {dir} создана")
    except FileExistsError:
        for dir in range(1, 10):
            print(f"директория {dir} уже создана!")
# make_dirs()

def del_dirs():
    try:
        for dir in range(1, 10):
            os.rmdir(f"dir_{dir}")
            print(f"Директория {dir} удалена")
    except FileNotFoundError:
        for dir in range(1, 10):
            print(f"директория {dir} уже удалена!")
# del_dirs()



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def path_info():
    for path in os.listdir('.'):
        if os.path.isdir(path):
            print(path)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    file_name = sys.argv[0].split('/')[-1]
    ending_file = file_name.split(".")[-1]
    copy_file = file_name.split('.')[0] + "_copy." + ending_file
    shutil.copyfile(file_name, copy_file)
    try:
        print(f"Файл {file_name} скопирован!")
    except:
        pass

copy_file()

do = {
    "help": print_help,
    "mkdirs": make_dirs,
    "del_dirs": del_dirs,
    "path_info": path_info,
    "copy_file": copy_file,
}

try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Ключ неверный. Укажите ключ help")