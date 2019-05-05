__author__ = 'Ушаков Михаил Викторович'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print("Путь - ", sys.argv)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("rmdir <dir_name> - удаление директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f"Директория {dir_name} создана")
    except FileExistsError:
        print(f"Директория {dir_name} уже создана")

def remove_dir():
    if not dir_name:
        print("Необходимо указать имя директории")
        return
    try:
        answer = input(f"Удалить файл {file_name} с вашего компьютера? Y/N ")
        if answer.upper() == "Y":
            os.rmdir(dir_name)
            print(f"Директория {dir_name} удалена")
        else:
            print(f"Файл {file_name} не удален!")

    except FileNotFoundError:
        print(f"Дириктории {dir_name} не существует!")
    except NotADirectoryError:
        print(f"{dir_name} - это не папка, удалить не удалось!")

def ping():
    print("pong")

def copy_file():
    if not file_name:
        print("Укажите имя файла.")
        return
    try:
        ending_file = file_name.split(".")[-1]
        copy_file = file_name.split('.')[0] + "_copy." + ending_file
        shutil.copyfile(file_name, copy_file)
        if os.path.exists(copy_file):
            print(f"Файл {file_name} скопирован")

    except FileNotFoundError:
        print(f"Файл {file_name} не существует!")

def remove_file():
    if not file_name:
        print("Укажите имя файла.")
        return
    try:
        answer = input(f"Удалить файл {file_name} с вашего компьютера? Y/N ")
        if answer.upper() == "Y":
            os.remove(file_name)
            print(f"Файл {file_name} успешно удален")
        else:
            print(f"Файл {file_name} не удален!")
    except FileNotFoundError:
        print(f"Файл {file_name} не существует!")

def go_to_folder():
    if not dir_name:
        print("Необходимо указать имя директории")
        return
    if os.path.isdir(dir_name):
        path = dir_name
    try:
        os.chdir(path)
        print(f"Вы перешли в директорию {path.split('/')[-1]}")
    except UnboundLocalError:
        print(f"Директории {dir_name} не существует!")

def full_path():
    print("Путь - ", os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": go_to_folder,
    "ls": full_path,
    "rmdir": remove_dir,
}

try:
    dir_name = sys.argv[2]
    file_name = sys.argv[2]
except IndexError:
    dir_name = None
    file_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Ключ неверный. Укажите ключ help")