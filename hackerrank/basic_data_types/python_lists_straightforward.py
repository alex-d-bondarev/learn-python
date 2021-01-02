program_list = []


def execute_command_with_params(input):
    command, params = input.split(sep=" ", maxsplit=1)

    if command == "insert":
        i, e = map(int, params.split(sep=" ", maxsplit=1))
        program_list.insert(i, e)

    if command == "remove":
        e = int(params)
        program_list.remove(e)

    if command == "append":
        e = int(params)
        program_list.append(e)


def execute_simple_command(input):
    if input == "print":
        print(program_list)

    if input == "sort":
        program_list.sort()

    if input == "pop":
        program_list.pop()

    if input == "reverse":
        program_list.reverse()


if __name__ == '__main__':
    commands = list()
    n = int(input())
    for _ in range(n):
        commands.append(input())

    for command in commands:
        if ' ' in command:
            execute_command_with_params(command)
        else:
            execute_simple_command(command)
