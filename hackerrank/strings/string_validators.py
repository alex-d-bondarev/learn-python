if __name__ == '__main__':
    s = input()

    has_al_num = has_alpha = has_digits = has_lower = has_upper = False

    for char in s:
        has_al_num = has_al_num or char.isalnum()
        has_alpha = has_alpha or char.isalpha()
        has_digits = has_digits or char.isdigit()
        has_lower = has_lower or char.islower()
        has_upper = has_upper or char.isupper()

    print(has_al_num)
    print(has_alpha)
    print(has_digits)
    print(has_lower)
    print(has_upper)
