def insertion_sort(list_to_sort):
    length = len(list_to_sort)

    for i in range(1, length):
        insert_index = i
        value_now = list_to_sort[i]

        for j in range(i - 1, -1, -1):
            if list_to_sort[j] > value_now:
                list_to_sort[j + 1] = list_to_sort[j]
                insert_index = j
            else:
                break
        list_to_sort[insert_index] = value_now

    return list_to_sort
