if __name__ == '__main__':
    first_set_size = int(input())
    first_set = set(map(int, input().split()))
    second_set_size = int(input())
    second_set = set(map(int, input().split()))

    # symmetric_difference = first_set.difference(second_set)
    # symmetric_difference.update(second_set.difference(first_set))
    # for x in sorted(symmetric_difference):
    #     print(x)

    print(*sorted(first_set ^ second_set, key=int), sep='\n')
