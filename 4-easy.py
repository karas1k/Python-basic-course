__author__ = 'Ушаков Михаил Викторович'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
import copy

# Решкние № 1
my_list = [random.randint(1, 20) for i in range(10)]
square_numbers = [i ** 2 for i in my_list]
print(my_list)
print(square_numbers)

#  Решение № 2
print("")
def random_list(range_random, range_list):
    my_list = [random.randint(1, range_random) for i in range(range_list)]
    square_list = copy.copy(my_list)
    square = 0
    for el in square_list:
        square = el ** 2
        print(f"Квадрат числа {el} = {square}")

random_list(15, 10)
print("")


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

first_list_fruits = ["банан", "яблоко", "мандарин", "арбуз", "груша"]
second_list_fruits = ["апельсин", "помeло", "ананас", "банан", "дыня", "груша", "мандарин"]
all_fruits = [fruit for fruit in first_list_fruits if fruit in second_list_fruits]
print(all_fruits)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

my_list = [random.randint(-10, 15) for i in range(10)]
finaly_list = [number for number in my_list if number % 3 == 0 and number > 0 and number % 4 != 0]
print(f"\n{my_list}")
print(f"\n{finaly_list}")