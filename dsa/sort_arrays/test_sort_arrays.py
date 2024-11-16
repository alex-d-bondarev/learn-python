import logging
import random
import sys
from copy import copy
from timeit import timeit

from dsa.sort_arrays.bubble_sort import breaking_buble_sort, simple_buble_sort
from dsa.sort_arrays.counting_sort import (
    counting_sort,
    counting_sort_v2,
    counting_sort_w3c,
)
from dsa.sort_arrays.hybrids import call_quicksort_so, quick_insertion_sort_hybrid
from dsa.sort_arrays.insertion_sort import insertion_sort
from dsa.sort_arrays.merge_sort import merge_sort_loop, merge_sort_req
from dsa.sort_arrays.quick_sort import call_quick_sort
from dsa.sort_arrays.radix_sort import rad_sort_w3c, simple_rad_sort
from dsa.sort_arrays.selection_sort import selection_sort

logger = logging.getLogger(__name__)

ALL_SORTING_FUNCTIONS = [
    simple_buble_sort,
    breaking_buble_sort,
    selection_sort,
    insertion_sort,
    call_quick_sort,
    counting_sort,
    counting_sort_v2,
    counting_sort_w3c,
    simple_rad_sort,
    rad_sort_w3c,
    merge_sort_req,
    merge_sort_loop,
    quick_insertion_sort_hybrid,
    call_quicksort_so,
]

# fmt: off
LIST_OF_40 = [82, 8, 5, 13, 11, 14, 14, 21, 97, 29, 32, 33, 39, 70, 73, 74, 91, 47, 44, 43, 42, 41, 40, 83, 73, 53, 68,
              67, 54, 81, 90, 63, 99, 100, 47, 55, 81, 82, 81, 53, ]
TINY_LIST = [8, 6, 10, 9, 7, 5]
SORTED_TINY_LIST = [5, 6, 7, 8, 9, 10]
# fmt: on’


def test_sorting():
    for sorter in ALL_SORTING_FUNCTIONS:
        assert sorter(copy(TINY_LIST)) == SORTED_TINY_LIST, sorter.__name__


def generate_random_large_list(max_val, size):
    max_val_r = range(max_val)
    return [random.choice(max_val_r) for _ in range(size)]


def test_performance():
    sys.setrecursionlimit(10_000)
    random_large_list = generate_random_large_list(max_val=1000, size=1000)

    run_for_a_list(
        sorters=ALL_SORTING_FUNCTIONS,
        list_to_sort=TINY_LIST,
        list_description="tiny list",
    )
    run_for_a_list(
        sorters=ALL_SORTING_FUNCTIONS,
        list_to_sort=LIST_OF_40,
        list_description="small list",
    )
    run_for_a_list(
        sorters=ALL_SORTING_FUNCTIONS,
        list_to_sort=random_large_list,
        list_description="large list",
    )


def run_for_a_list(sorters: list, list_to_sort: list, list_description: str) -> None:
    results = dict()
    logger.info("\nRun on a %s\n", list_description)

    for sorter in sorters:
        results[sorter.__name__] = run_sorting_performance_test(sorter, list_to_sort)

    fastest_k = key_with_smallest_value(results)
    logger.info(
        "The winner of '%s' sorting is %s with %s runtime",
        list_description,
        fastest_k,
        results[fastest_k],
    )

    logger.info("A bonus default sort function")
    run_sorting_performance_test(sorted, list_to_sort)


def key_with_smallest_value(d: dict):
    return min(d, key=d.get)


def run_sorting_performance_test(func, unsorted_list):
    times = 100
    average_time = measure_the_average(func, unsorted_list, times)

    result = f"{func.__name__}() runs {average_time}ms on average after {times} runs"
    logger.info(result)

    return average_time


def measure_the_average(func, unsorted_list, times: int):
    stmt = f"{func.__name__}({copy(unsorted_list)})"
    total_time = timeit(stmt=stmt, number=times, globals=globals())
    return f"{((total_time / times) * 1000):.6f}"
