from collections import deque

if __name__ == '__main__':
    d = deque()

    for _ in range(int(input())):
        inputs = input().split(" ", 1)
        if len(inputs) > 1:
            values = inputs[1:] if len(inputs) > 1 else []
            command = f"d.{inputs[0]}(\",\".join(values))"
        else:
            command = f"d.{inputs[0]}()"

        eval(command)

    print(*d)
