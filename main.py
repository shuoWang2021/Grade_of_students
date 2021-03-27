# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
    This project is to simulate the case containing the grades of any student,
    which have different subjects with different weight having different score
    and weight of score, and then could analyse the sum of scores and its average.

    Class Grade_Book contains all information of student
    Class Student contains all subjects with different scores and weight
    Class Score_weight contains all scores and weights by using namedtuple

    I import two classes namedtuple and defaultdict from Method collections,
    I use namedtuple as the base-level-container,
    I use defaultdict as the container of any unknown named instance of class student,
    as well as the container of any unknown named instance of class subject.
"""

from collections import defaultdict, namedtuple

Grade = namedtuple('Grade', ('score', 'weight_score'))


class Subject:
    """
        A instance of Subject has any numbers of namedtuple elements with two members,
        score and weight_score of each. I use list[] to contain them, named grades.
        In case of subjects have different weight, i have an attribute, named subject_weight,
        initialized when the instance is initialized(means in __init__ function).
        Because of __init__ has an outer argument, i have to supplement a class to call it, named Subject_dict(dict)
    """

    def __init__(self):
        self._grades = []

    def report_grades(self, score, weight_score):
        self._grades.append(Grade(score, weight_score))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight_score
            total_weight += grade.weight_score
        return total / total_weight

class Student:
    # Every student have any numbers of Subject_Dict with different weight of each subject.
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def add_subjects(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Grade_Book:
    # A grade book have any numbers of students.
    def __init__(self):
        self._students = defaultdict(Student)
    def add_student(self,name):
        return self._students[name]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    book_1 = Grade_Book()
    student_1 = book_1.add_student('Shuo WANG')
    math = student_1.add_subjects('Math')
    math.report_grades(99,0.1)
    math.report_grades(100,0.9)
    math.report_grades(80,0.4)
    physics = student_1.add_subjects('physics')
    physics.report_grades(100,1)
    print(student_1.average_grade())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
