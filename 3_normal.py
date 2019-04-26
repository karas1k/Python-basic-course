__author__ = 'Ушаков Михаил Викторович'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = 0
    b = 1
    my_list = []
    for el in range(0, m): # формируем в цикле список чисел Фибоначчи
        my_list.append(b)
        c = a # вводим третью переменную для сложения предыдущих 2 чисел и получения следующего
        a = b # записываем последнее число Фи в переменную а
        b += c # складываем 2 числа Фи, получаем новое
    for i in range(n - 1, m): # уменьшаем n на 1, так как отсчет в списке идет с 0
        print(my_list[i], end=', ')

fibonacci(5, 10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for el in range(len(origin_list)):
        for i in range(len(origin_list) - 1, el, -1):
            if origin_list[i] < origin_list[i - 1]:
                sub_list = origin_list[i]
                origin_list[i] = origin_list[i - 1]
                origin_list[i - 1] = sub_list
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Решение №2

print("\nРешение №2")
def sort_to_max(origin_list):
    origin_list = sorted(origin_list)
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


print("\nЗадача №3")

def my_filtr(first_list, filter):
    print (first_list)
    my_list = []
    for i in first_list :
        if i < filter:
            my_list.append(i)
    print (my_list)

first_list = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11 ,11, 12]

my_filtr(first_list, 10)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

