def simple_rad_sort(list_to_sort):
    radix_buckets = [[] for _ in range(10)]
    list_length = len(list_to_sort)
    max_num = max(list_to_sort)
    slice_index = 1

    while max_num // slice_index > 0:
        for _ in range(list_length):
            value = list_to_sort.pop()
            value_radix = (value // slice_index) % 10
            radix_buckets[value_radix].append(value)

        for bucket in radix_buckets:
            for _ in range(len(bucket)):
                list_to_sort.append(bucket.pop())

        slice_index *= 10

    return list_to_sort


def rad_sort_w3c(my_array):
    # From https://www.w3schools.com/dsa/dsa_algo_radixsort.php
    radix_array = [[] for _ in range(10)]
    max_val = max(my_array)
    exp = 1

    while max_val // exp > 0:

        while len(my_array) > 0:
            val = my_array.pop()
            radix_index = (val // exp) % 10
            radix_array[radix_index].append(val)

        for bucket in radix_array:
            while len(bucket) > 0:
                val = bucket.pop()
                my_array.append(val)

        exp *= 10

    return my_array
