def partition(list_to_sort, low, high):
    pivot = list_to_sort[high]
    i = low - 1

    for j in range(low, high):
        if list_to_sort[j] <= pivot:
            i += 1
            if i != j:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]

    list_to_sort[i + 1], list_to_sort[high] = list_to_sort[high], list_to_sort[i + 1]
    return i + 1


def quicksort(list_to_sort, low=0, high=None):
    if high is None:
        high = len(list_to_sort) - 1

    if low < high:
        pivot_index = partition(list_to_sort, low, high)
        quicksort(list_to_sort, low, pivot_index - 1)
        quicksort(list_to_sort, pivot_index + 1, high)


def call_quick_sort(list_to_sort):
    quicksort(list_to_sort)
    return list_to_sort


def debug_call_q_s():
    debug_list = [8, 6, 10, 9, 7, 5]
    quicksort(debug_list)
    print(debug_list)
