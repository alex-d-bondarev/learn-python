if __name__ == '__main__':
    the_list = list()
    for _ in range(int(input())):
        text = input().split()
        command = text[0]
        arguments = text[1:]
        if command == "print":
            print(the_list)
        else:
            command += "(" + ",".join(arguments) + ")"
            eval("the_list." + command)
