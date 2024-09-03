if __name__ == '__main__':
    a_set_size = input()
    a_set = set(map(int, input().split()))

    for _ in range(int(input())):
        operation = input().split()[0]
        command = "a_set." + operation + "([" + ",".join(input().split()) + "])"
        eval(command)

    print(sum(a_set))
