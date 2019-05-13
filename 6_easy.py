__author__ = 'Ушаков Михаил Викторович'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# Обозначим координаты точек, определяющих треугольник, как A(x₁,y₁), B(x₂,y₂) и C(x₃,y₃)

import math as m

class Triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def square(self):
        S = 0.5 * (m.fabs((self.x2 - self.x1) * (self.y3 - self.y1) -
                   (self.x3 - self.x1) * (self.y2 - self.y1)))

        return (f"Площадь треугольника = {S}")

    def perimetr(self):
        """Вычислим длины сторон треугольника"""
        self.AB = round(m.sqrt(m.fabs(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))), 2)
        self.BC = round(m.sqrt(m.fabs(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))), 2)
        self.AC = round(m.sqrt(m.fabs(((self.x3 - self.x1) ** 2) + ((self.y3 - self.y1) ** 2))), 2)
        # print("AB = ", self.AB) для проверки в онлайн калькуляторе
        # print("BC = ", self.BC) для проверки в онлайн калькуляторе
        # print("AC = ", self.AC) для проверки в онлайн калькуляторе

        self.P = self.AB + self.BC + self.AC
        return (f"Периметр треугольника = {self.P}")

    def height(self):
        """Вычислим полупериметр p"""
        p = 0.5 * self.P

        """Вычислим высоту треугольника из всех точек"""

        hA = round((2 * m.sqrt(p * (p - self.AB) * (p - self.BC) * (p - self.AC))) / self.AB, 2)
        hB = round((2 * m.sqrt(p * (p - self.AB) * (p - self.BC) * (p - self.AC))) / self.BC, 2)
        hC = round((2 * m.sqrt(p * (p - self.AB) * (p - self.BC) * (p - self.AC))) / self.AC, 2)

        print(f"Высота из точки А = {hA}")
        print(f"Высота из точки B = {hB}")
        print(f"Высота из точки C = {hC}")



triangle1 = Triangle(0, 0, 8, 2, -2, 6)
print(triangle1.square())
print(triangle1.perimetr())
triangle1.height()
print("\n--------------------------\n")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze(Triangle):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

        """Вычислим длины сторон трапеции"""

        self.AB = round(m.sqrt(m.fabs(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))), 2)
        self.BC = round(m.sqrt(m.fabs(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))), 2)
        self.CD = round(m.sqrt(m.fabs(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))), 2)
        self.DA = round(m.sqrt(m.fabs(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))), 2)

        print(f"Длина стороны AB = {self.AB}")
        print(f"Длина стороны BC = {self.BC}")
        print(f"Длина стороны CD = {self.CD}")
        print(f"Длина стороны DA = {self.DA}")

    def equilateral(self):
        if self.BC == self.DA:
            return "Фигура является равнобокой трапецией"
        else:
            return "Фигура НЕ является равнобокой трапецией"

    def perimeter(self):
        self.P = round(self.AB + self.BC + self.CD + self.DA, 2)
        return (f"Периметр трапеции = {self.P}")

    def square(self):
        self.h = self.BC / 2 # Высота трапеции
        if self.BC == self.DA:
            self.S = round((0.5 * (self.AB + self.CD)) * self.h, 2) # Площадь трапеции
            return (f"Площадь трапеции = {self.S}")
        else:
            a = self.AB
            b = self.CD
            c = self.DA
            d = self.BC
            self.S = round(0.5 * (self.AB + self.CD) * m.sqrt((c ** 2) - ((((b - a) ** 2) +
                                            (c ** 2) - (d ** 2)) / (2 * ( b - a)) ** 2)))
            return (f"Площадь разнобокой трапеции = {self.S}")


trapeze1 = Trapeze(0, 3, 0, 7, 8, 15, 2, 44)
print(trapeze1.equilateral())
print(trapeze1.perimeter())
print(trapeze1.square())
print("\n--------------------------\n")
trapeze2 = Trapeze(0, 2, 0, 7, 2, 5, 2, 4)
print(trapeze2.equilateral())
print(trapeze2.perimeter())
print(trapeze2.square())
print("\n--------------------------\n")
trapeze3 = Trapeze(-4, 2, 4, 2, -4, 6, 4, 6)
print(trapeze3.equilateral())
print(trapeze3.perimeter())
print(trapeze3.square())