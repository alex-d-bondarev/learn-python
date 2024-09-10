
def simple_buble_sort(list_to_sort):
    length = len(list_to_sort)

    for right_limit in range(length - 1):
        for now in range(length - right_limit - 1):
            if list_to_sort[now] > list_to_sort[now + 1]:
                list_to_sort[now], list_to_sort[now + 1] = list_to_sort[now + 1], list_to_sort[now]

    return list_to_sort


def breaking_buble_sort(list_to_sort):
    length = len(list_to_sort)

    for right_limit in range(length - 1):
        swapped = False
        for now in range(length - right_limit - 1):
            if list_to_sort[now] > list_to_sort[now + 1]:
                list_to_sort[now], list_to_sort[now + 1] = list_to_sort[now + 1], list_to_sort[now]
                swapped = True

        if not swapped:
            break

    return list_to_sort
