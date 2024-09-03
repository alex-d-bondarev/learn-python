def print_door_mat():
    pattern = ".|."
    lines_num, line_width = map(int, input().split())

    pattern_size = 1

    for i in range(lines_num // 2):
        print((pattern * pattern_size).center(line_width, '-'))
        pattern_size += 2

    print("WELCOME".center(line_width, '-'))

    for i in range(lines_num // 2):
        pattern_size -= 2
        print((pattern * pattern_size).center(line_width, '-'))


if __name__ == '__main__':
    print_door_mat()
