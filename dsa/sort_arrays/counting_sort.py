from collections import Counter


def counting_sort_simple(list_to_sort):
    max_value = max(list_to_sort)
    counter = [0] * (max_value + 1)

    for value in list_to_sort:
        counter[value] += 1

    sorted_list = list()
    for index, counted in enumerate(counter):
        sorted_list = sorted_list + [index] * counted

    return sorted_list


def counting_sort_w3c(arr):
    # From https://www.w3schools.com/dsa/dsa_algo_countingsort.php
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr
