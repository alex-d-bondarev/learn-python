def gcd_division(a, b):
    while b != 0:
        remainder = a % b
        print(f"{a} = {a//b} * {b} + {remainder}")
        a = b
        b = remainder
    return a


def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            print(f"{a} - {b} = {a-b}")
            a = a - b
        else:
            print(f"{b} - {a} = {b-a}")
            b = b - a
    return a


def test_w3c_case():
    a = 120
    b = 25

    print("The Euclidean algorithm using division:\n")
    result = gcd_division(a, b)
    print(f"The GCD of {a} and {b} is: {result}")
    assert result == 5

    print("The Euclidean algorithm using subtraction:\n")
    result = gcd_subtraction(a, b)
    print(f"The GCD of {a} and {b} is: {result}")
    assert result == 5
