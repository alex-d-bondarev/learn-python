def get_alphabet_line(start, stop):
    alphabet_line = ""
    for i in range(start - 1, stop - 1, -1):
        alphabet_line += chr(ord('a') + i) + '-'

    for i in range(stop + 1, start):
        alphabet_line += chr(ord('a') + i) + '-'

    return alphabet_line[:-1]


def print_rangoli(size):
    line_width = (size - 1) * 4 + 1
    for i in range(size - 1, 0, -1):
        print(get_alphabet_line(size, i).center(line_width, '-'))

    print(get_alphabet_line(size, 0).center(line_width, '-'))

    for i in range(1, size):
        print(get_alphabet_line(size, i).center(line_width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
