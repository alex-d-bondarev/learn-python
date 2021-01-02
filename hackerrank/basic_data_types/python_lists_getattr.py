if __name__ == '__main__':
    the_list = list()
    for _ in range(int(input())):
        command, *args = input().split()
        try:
            getattr(the_list, command)(*(int(arg) for arg in args))
        except AttributeError:
            print(the_list)
