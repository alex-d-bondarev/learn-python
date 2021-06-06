from collections import Counter


def initial_solution():
    number_of_shoes = int(input())
    sizes = input().split()
    number_of_customers = int(input())

    all_shoes = dict(Counter(sizes))
    earned_money = 0

    for _ in range(number_of_customers):
        size, money = input().split()
        if size in all_shoes and all_shoes[size] > 0:
            earned_money += int(money)
            all_shoes[size] = all_shoes[size] - 1

    print(earned_money)


def shorter_solution():
    number_of_shoes = int(input())
    sizes = input().split()

    all_shoes = Counter(sizes)
    earned_money = 0

    for _ in range(int(input())):
        size, money = input().split()
        if all_shoes[size]:
            earned_money += int(money)
            all_shoes[size] -= 1

    print(earned_money)


if __name__ == '__main__':
    # initial_solution()
    shorter_solution()
