if __name__ == '__main__':
    initial_set_size = int(input())
    initial_set = set(map(int, input().split()))
    for _ in range(int(input())):
        text = input().split()
        command = "initial_set." + text[0] + "(" + "".join(text[1:]) + ")"
        eval(command)

    print(sum(initial_set))
