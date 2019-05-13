__author__ = 'Ушаков Михаил Викторович'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, school_name, school_adress, teachers, students):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if person.get_class_room in
                           teachers.get_classes]
                parents = person.get_parents

                return {
                        'full_name': student_full_name,
                        'class_room': person.get_class_room,
                        'teachers': teachers,
                        'lessons': lessons,
                        'parents': parents
                        }

    @property
    def name(self):
        return f"Тарусская средняя школа {self._school_name}"

    @property
    def adress(self):
        return self._school_adress


class People:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    @property
    def get_full_name(self):
        return f"{self._last_name} {self._first_name} {self._middle_name}"

    @property
    def get_short_name(self):
        return f"{self._last_name} {self._first_name[:1]} {self._middle_name[:1]}"

class Student(People):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mather, father):
        People.__init__(self, last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
                        'mather': mather,
                        'father': father
                        }

    @property
    def get_class_room(self):
        return self._class_room

    @property
    def get_parents(self):
        return self._parents


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name,
                 courses, classes):
        People.__init__(self, last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes

    @property
    def get_courses(self):
        return self._courses

    @property
    def get_classes(self):
        return self._classes


teachers = [
            Teacher('Неволина', 'Татьяна', 'Владимировна', 'Русский язык',
                    ['9А', '9Б', '10А', '10Б', '11А', '11Б']),
            Teacher('Филипова', 'Татьяна', 'Николаевна', 'Физика',
                    ['10А', '10Б', '11А', '11Б']),
            Teacher('Нацис', 'Людмила', 'Петровна', 'Немецкий язык',
                    ['8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б']),
            ]

students = [
            Student('Ушаков', 'Михаил', 'Викторович', '11Б',
                    'Ушаков В.М.', 'Ушакова О.В.'),
            Student('Суханов', 'Иван', 'Алексеевич', '11Б',
                    'Суханов А.И.', 'Суханова Н.А.'),
            Student('Шумаков', 'Павел', 'Вячаславович', '9Б',
                    'Шумаков В.Ю.', 'Шумакова М.Г.'),
            Student('Саевец', 'Николай', 'Николаевич', '8А',
            'Саевец Н.Н.', 'Саевец И.В.'),
            Student('Саевец', 'Артем', 'Николаевич', '10А',
            'Саевец Н.Н.', 'Саевец И.В.'),
            ]

school = School('ТСШ №1', 'г.Таруса, ул.Ленина 72', teachers, students)

print(school.name)
print(school.adress)

print(f"\nСписок классов школы:\n{', '.join(school.get_all_classes())}")

print(f"\nСписок учеников 11Б класса:\n{', '.join(school.get_students('11Б'))}")

print("\n-------------------\n")

student = school.find_student('Ушаков Михаил Викторович')
print(f"Ученик: {student['full_name']}\nКласс: {student['class_room']}\n"
      f"Преподаватели: {', '.join(student['teachers'])}\nПредметы: {', '.join(student['lessons'])}")


print('Родители: {0}, {1}'.format(student['parents']['mather'],
                                  student['parents']['father']))

print(f"\nКласс: 10A\nПреподаватели: {', '.join(school.get_teachers('10А'))}")