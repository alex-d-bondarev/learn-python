if __name__ == '__main__':
    test_cases_amount = int(input())

    for _ in range(test_cases_amount):
        a_set_size = int(input())
        a_set = set(map(int, input().split()))
        b_set_size = int(input())
        b_set = set(map(int, input().split()))

        print(a_set.issubset(b_set))
