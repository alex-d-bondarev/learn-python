"""4 lines of code are not very readable"""
from collections import namedtuple

if __name__ == '__main__':
    number_of_students = int(input())
    Student = namedtuple("Student", input().split())
    scores = []

    for _ in range(number_of_students):
        scores.append(int(Student(*input().split()).MARKS))

    print("%.2f" % (sum(scores) / number_of_students))
