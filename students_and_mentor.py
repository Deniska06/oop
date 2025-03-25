class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def counting_average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        avg_grade = self.counting_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет завершенных курсов"
        return f"ФИО: {self.surname} {self.name} \nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.counting_average_grade() < other.counting_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.counting_average_grade() == other.counting_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def __str__(self):
        return f"ФИО: {self.surname} {self.name}"

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.counting_average_grade()
        courses_attached = ', '.join(self.courses_attached) if self.courses_attached else "Нет закрепленных курсов"
        return super().__str__() + f"\n Средняя оценка за лекции: {avg_grade}\n Закрепленные курсы: {courses_attached}"

    def counting_average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return super().__str__()

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def counting_average_hw_grade(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    return round(sum(grades) / len(grades), 1) if grades else 0

def counting_average_lec_grade(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    return round(sum(grades) / len(grades), 1) if grades else 0

student1 = Student('Иван', 'Иванов', 'Муж')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['SMM']

student2 = Student('Ирина', 'Какетка', 'Жен')
student2.courses_in_progress += ['Python', 'Git']

lecturer1 = Lecturer('Фёдор', 'Пупкин')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Тася', 'Кошкина')
lecturer2.courses_attached += ['Git']

сhecking1 = Reviewer('Тася', 'Кошкина')
сhecking1.courses_attached += ['Python']

сhecking2 = Reviewer('Хуан', 'Карлос')
сhecking2.courses_attached += ['Git']

сhecking1.rate_hw(student1, 'Python', 8)
сhecking1.rate_hw(student1, 'Python', 7)
сhecking1.rate_hw(student2, 'Python', 6)

student1.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer1, 'Python', 9)

student1.rate_lecture(lecturer2, 'Git', 5)
student2.rate_lecture(lecturer2, 'Git', 6)

print("Проверяющие:")
print(сhecking1)
print(сhecking2)
print("=====", "\n")
print("Лекторы:")
print(lecturer1)
print(lecturer2)
print("=====", "\n")
print("Студенты:")
print(student1)
print("=====", "\n")
print(student2)
print("=====", "\n")
# print("")
if student1 > student2:
    print(f'У студента: {student1.surname} {student1.name} средняя оценка {student1.counting_average_grade()} выше, чем у {student2.surname} {student2.name} {student2.counting_average_grade()}')
else:
    print(f'У студента: {student2.surname} {student2.name} средняя оценка {student2.counting_average_grade()} выше, чем у {student1.surname} {student1.name} {student1.counting_average_grade()}')

students = [student1, student2]
average_hw_grade = counting_average_hw_grade(students, 'Python')
print(f"\nСредняя оценка за домашние задания всех студентов по курсу Python: {average_hw_grade}")

lecturers = [lecturer1, lecturer2]
average_lec_grade = counting_average_lec_grade(lecturers, 'Python')
print(f"Средняя оценка за лекции всех лекторов по курсу Python: {average_lec_grade}")