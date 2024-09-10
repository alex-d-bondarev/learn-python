def merge_sort_req(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort

    slicer = len(list_to_sort) // 2
    left = list_to_sort[:slicer]
    right = list_to_sort[slicer:]

    left = merge_sort_req(left)
    right = merge_sort_req(right)

    return merge(left, right)


def merge_sort_loop(list_to_sort):
    step = 1
    length = len(list_to_sort)

    while step < length:
        for i in range(0, length, step * 2):
            left = list_to_sort[i:i + step]
            right = list_to_sort[i + step:i + step * 2]

            merged = merge(left, right)
            for j, value in enumerate(merged):
                list_to_sort[i + j] = value
        step *= 2
    return list_to_sort


def merge(left, right):
    sorted_list = list()
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list
