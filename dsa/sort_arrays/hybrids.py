THRESHOLD = 50


def partition_for_hybrid(list_to_sort, low, high):
    pivot = list_to_sort[high]
    i = low - 1

    for j in range(low, high):
        if list_to_sort[j] <= pivot:
            i += 1
            if i != j:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]

    list_to_sort[i + 1], list_to_sort[high] = list_to_sort[high], list_to_sort[i + 1]
    return i + 1


def insertion_sort_for_hybrid(list_to_sort, low=0, high=None):
    if not high:
        high = len(list_to_sort)

    for i in range(low + 1, high):
        insert_index = i
        value_now = list_to_sort[i]

        for j in range(i - 1, low - 1, -1):
            if list_to_sort[j] > value_now:
                list_to_sort[j + 1] = list_to_sort[j]
                insert_index = j
            else:
                break
        list_to_sort[insert_index] = value_now


def quick_sort_for_hybrid(list_to_sort, low=0, high=None):
    if high is None:
        high = len(list_to_sort) - 1

    if low < high:
        pivot_index = partition_for_hybrid(list_to_sort, low, high)
        middle_high = pivot_index - 1
        middle_low = pivot_index + 1
        if middle_low - low < THRESHOLD:
            insertion_sort_for_hybrid(list_to_sort, low, middle_high)
        else:
            quick_sort_for_hybrid(list_to_sort, low, middle_high)

        if high - middle_high < THRESHOLD:
            insertion_sort_for_hybrid(list_to_sort, middle_low, high)
        else:
            quick_sort_for_hybrid(list_to_sort, middle_low, high)


def quick_insertion_sort_hybrid(list_to_sort):
    if len(list_to_sort) < THRESHOLD:
        insertion_sort_for_hybrid(list_to_sort)
    else:
        quick_sort_for_hybrid(list_to_sort)
    return list_to_sort

# From https://stackoverflow.com/a/71086616/8661297


def insertion_sort_so(arr, low, high):
    for i in range(low + 1, high + 1):
        j = i
        while j > low and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def quicksort_so(a, low=0, high=None):
    if high is None:
        high = len(a) - 1

    if low < high:
        if high - low + 1 < THRESHOLD:
            # Size of the subarray is less than the threshold, insertion sort
            insertion_sort_so(a, low, high)
            return
        # Size of the subarray is greater than the threshold, quicksort
        pivot_index = partition_for_hybrid(a, low, high)
        print("The pivot_index is:", pivot_index)
        print("Low is:", low)
        print("High is:", high)
        quicksort_so(a, low, pivot_index - 1)
        quicksort_so(a, pivot_index + 1, high)


def call_quicksort_so(list_to_sort):
    quicksort_so(list_to_sort)
    return list_to_sort
