
import os

def go_to_folder():
    path = input("Введите путь к директории: ")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"Вы перешли в директорию '{path.split('/')[-1]}'")
    else:
        print(f"Директории '{path.split('/')[-1]}' не существует!")


def view_folder():
    elements = []
    for element in os.listdir():
        elements.append(element)
    print("Список элементов директории:\n")
    for el in elements:
        print(el)

def make_dir():
    dir_name = input('Введите название для новой директории: ')
    if not dir_name:
        print("Необходимо указать имя директории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f"Директория '{dir_name}' создана")
    except FileExistsError:
        print(f"Директория '{dir_name}' уже создана")



def delete_dir():
    dir_name = input('Введите название папки, которую хотите удалить: ')
    if not dir_name:
        print("Необходимо указать имя директории")
        return
    try:
        os.rmdir(dir_name)
        print(f"Директория '{dir_name}' удалена")
    except FileNotFoundError:
        print(f"Дириктории '{dir_name}' не существует!")
    except NotADirectoryError:
        print(f"'{dir_name}' - это не папка, удалить не удалось!")
