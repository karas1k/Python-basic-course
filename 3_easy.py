__author__ = 'Ушаков Михаил Викторович'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# number = 2.1234567 # исходное число
# ndigits = 5 # - кол-во знаков для округления
# number *= 100000 # умножаю на 10 в степени 5 (кол-во знаков для округления)
# number += 0.4 # прибавляю 0,4, если последние цифры > 5, то последние цифры увеличатся
# number //= 1 # откидываю от числа дробную часть
# number /= 100000 # возвращаю число к исходному виду поделив на 10 в степени 5 (кол-во знаков для округления)
# print(number)

def my_round(number, ndigits):
    number *= 10 ** ndigits # умножаю исходное число на 10 в степени равном числу знаков для округления (5)
    number += 0.4 # увеличиваю число на 0.4 что бы округлить если последние цифры более 5
    number //= 1 # откидываю от числа дробную часть
    return number / 10 ** ndigits # возвращаю число к исходному виду поделив на 10 в степени 5

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

print("\nРешение №2")
def my_round(number, ndigits):
    number = round(number, ndigits)
    # number = number.__round__(ndigits) - так тоже работает, случайно ввел с __
    return number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# a = 123006
# a = list(enumerate(str(a)))
# if int(a[0][1]) + int(a[1][1]) + int(a[2][1]) == int(a[3][1]) + int(a[4][1]) + int(a[5][1]):
#     print("Lucky")
# else:
#     print('Looser')

def lucky_ticket(ticket_number):
    ticket_number = list(enumerate(str(ticket_number)))
    if len(ticket_number) < 6 or len(ticket_number) > 6:
        return "Loose"
    elif int(ticket_number[0][1]) + int(ticket_number[1][1]) + int(ticket_number[2][1]) ==\
            int(ticket_number[3][1]) + int(ticket_number[4][1]) + int(ticket_number[5][1]):
        return "Lucky"
    else:
        return "Loose"

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(43675123123123213123121231))
print(lucky_ticket(43))