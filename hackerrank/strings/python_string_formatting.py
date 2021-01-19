def print_formatted(number):
    results = []

    for i in range(1, number + 1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hexadecimal = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])

        results.append([decimal, octal, hexadecimal, binary])

    max_width = len(results[-1][3])

    for result_line in results:
        print(*(num.rjust(max_width) for num in result_line))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
