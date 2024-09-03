from collections import OrderedDict


def initial_solution():
    items = OrderedDict()
    for _ in range(int(input())):
        row = input().split()
        name = " ".join(row[0:-1])
        price = row[-1]
        if name in items:
            items[name] += int(price)
        else:
            items[name] = int(price)
    for name, price in items.items():
        print(f"{name} {price}")


def improved_solution():
    items = OrderedDict()
    for _ in range(int(input())):
        name, price = input().rsplit(" ", 1)
        items[name] = items.get(name, 0) + int(price)
    for name, price in items.items():
        print(name, price)


if __name__ == '__main__':
    improved_solution()
