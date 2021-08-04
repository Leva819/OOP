class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hm_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_for_lecturer:
                lecturer.grades_for_lecturer[course] += grade
            else:
                lecturer.grades_for_lecturer[course] = grade
        elif grade > 10:
            return 'Оценка не может быть больше 10!!!'
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции:{self.average_grade_st}, \nКурсы в процессе изучения: {self.courses_in_progress}, \nЗавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lecturer = {}
        self.average_grade = []

    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции:{self.average_grade}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.average_grade < other.average_grade




class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)


    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}'


Oleg = Lecturer('Олег', 'Булыгин')
Igor = Lecturer('Игорь', 'Акинфеев')

Sveta = Reviewer('Светлана', 'Ромашина')
Katya = Reviewer('Екатерина', 'Великая')

Vadim = Student('Вадим', 'Киселев', 'муж')
Vadim.grades = {'Python': 5}
Tanya = Student('Татьяна', 'Тимошенко', 'жен')
Tanya.grades = {'Python': 10}
list_ = [Vadim, Tanya]


def average_grade_of_students(list_of_students):
    grades = 0
    for student in list_of_students:
        for key, value in student.grades.items():
            grades += value
    print(grades / len(list_of_students))

def average_grade_of_lecturers(list_of_lecturers):
    grades = 0
    for lecturer in list_of_lecturers:
        for key, value in lecturer.grades_for_lecturer.items():
            grades += value
    print(grades / len(list_of_lecturers))

average_grade_of_lecturers(list_2)
