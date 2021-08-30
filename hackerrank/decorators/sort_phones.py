def wrapper(f):
    def fun(l):
        decorated_numbers = []
        for number in l:
            decorated_numbers.append("+91 " + number[-10:-5] + " " + number[-5:])
        return f(decorated_numbers)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
