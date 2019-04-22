__author__ = 'Ушаков Михаил Викторович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("Задача № 1")

fruits = ["яблоко", "банан", "киви", "арбуз", "апельсин", "мандарин", "груша", "ананас"]
i = -1
for n in fruits:
    i += 1
    print("{} {:>8}".format(str(i + 1) + ".", n))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("\nЗадача № 2")

first_list = ["яблоко", "банан", "киви", "арбуз", "апельсин", "мандарин", "груша", "ананас"]
second_list = ["манго", "банан", "персик", "арбуз", "грейпфрут", "мандарин", "помело", "ананас"]
print("\nfirst_list = ",first_list)
print("second_list = ",second_list)

for f in first_list:
    if f in second_list:
        first_list.remove(f)

print("\nfirst_list = ",first_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("\nЗадача № 3")

# Создаю простой список от 1 до введенного числа включительно
number = int(input("\nВведите целое число "))
generate_list = []
lenth_list = range(1, number + 1)

for n in lenth_list: # Итерирую от 1 до введеного числа
    if n % 2 == 0: # Если число кратно 2, то поделим на 4
        n /= 4
    else:
        n *= 2 # Если число не кратно 2, то умножим на 2
    generate_list.append(n)
print(f"Наш список: {generate_list}")