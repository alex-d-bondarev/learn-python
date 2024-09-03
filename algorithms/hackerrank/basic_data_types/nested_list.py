def solution1():
    all_students = list()
    scores_list = list()
    results = list()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_students.append([name, score])

    for student in all_students:
        scores_list.append(student[1])

    second_score = sorted(set(scores_list))[1]
    for student in all_students:
        if student[1] == second_score:
            results.append(student[0])

    for name in sorted(results):
        print(name)


def solution2():
    all_students = []
    scores_set = set()
    results = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_students.append([name, score])
        scores_set.add(score)

    second_score = sorted(scores_set)[1]

    for name, score in all_students:
        if score == second_score:
            results.append(name)

    for name in sorted(results):
        print(name)


if __name__ == '__main__':
    solution2()
