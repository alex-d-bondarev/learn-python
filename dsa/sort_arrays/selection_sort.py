def selection_sort(list_to_sort):
    length = len(list_to_sort)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if list_to_sort[j] < list_to_sort[min_index]:
                min_index = j
        list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]

    return list_to_sort
