import string


def print_rangoli(size):
    alphabet = string.ascii_lowercase
    line_width = size * 4 - 3
    for i in range(size - 1, -size, -1):
        stop = abs(i)
        alphabet_line = '-'.join(alphabet[size - 1: stop:-1] +
                                 alphabet[stop:size])
        print(alphabet_line.center(line_width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
