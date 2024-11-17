from timeit import timeit
from typing import NamedTuple, Optional


class Item(NamedTuple):
    weight: int
    price: int


class Result(NamedTuple):
    price: int
    weight: int
    items: list[Item]


NO_ITEMS = []
THREE_ITEMS = [
    Item(weight=1, price=1),
    Item(weight=2, price=2),
    Item(weight=5, price=10),
]
# From https://www.w3schools.com/dsa/dsa_ref_knapsack.php
W3C_ITEMS = [
    Item(weight=2, price=300),
    Item(weight=1, price=200),
    Item(weight=5, price=400),
    Item(weight=3, price=500),
]
HUGE_ITEMS = [
    Item(weight=2, price=300),
    Item(weight=1, price=200),
    Item(weight=50, price=50_000),
    Item(weight=30, price=30_000),
]
MANY_ITEMS = [
    Item(weight=1, price=1),
    Item(weight=1, price=2),
    Item(weight=2, price=2),
    Item(weight=2, price=4),
    Item(weight=3, price=3),
    Item(weight=3, price=6),
    Item(weight=4, price=4),
    Item(weight=4, price=8),
    Item(weight=5, price=5),
    Item(weight=5, price=10),
    Item(weight=6, price=6),
    Item(weight=6, price=12),
    Item(weight=50, price=50_000),
    Item(weight=30, price=30_000),
    Item(weight=10, price=10),
    Item(weight=10, price=20),
    Item(weight=50, price=50_000),
    Item(weight=30, price=30_000),
    Item(weight=1, price=1),
    Item(weight=1, price=2),
    Item(weight=2, price=2),
    Item(weight=2, price=4),
    Item(weight=3, price=3),
    Item(weight=3, price=6),
    Item(weight=4, price=4),
    Item(weight=4, price=8),
    Item(weight=5, price=5),
    Item(weight=5, price=10),
    Item(weight=6, price=6),
    Item(weight=6, price=12),
    Item(weight=50, price=50_000),
    Item(weight=30, price=30_000),
    Item(weight=10, price=10),
    Item(weight=10, price=20),
    Item(weight=50, price=50_000),
    Item(weight=30, price=30_000),
    Item(weight=2, price=10),
    Item(weight=1, price=20),
    Item(weight=1, price=30),
    Item(weight=1, price=40),
    Item(weight=3, price=50),
    Item(weight=1, price=60),
    Item(weight=4, price=100),
]


# ==== Brute force loop


def loop_bf(items: list[Item], capacity) -> Result:
    all_results: list[Result] = [Result(price=0, weight=0, items=[])]
    for item in items:
        for current_result in all_results.copy():
            if current_result.weight + item.weight <= capacity:
                new_entry = Result(
                    price=current_result.price + item.price,
                    weight=current_result.weight + item.weight,
                    items=[*current_result.items, item],
                )
                all_results.append(new_entry)

    max_result = all_results.pop()
    for result in all_results:
        if result.price > max_result.price:
            max_result = result

    return max_result


# ==== Brute force recursion


def recursion_bf(
    all_items: list[Item], capacity, accumulated_results: Optional[list[Result]] = None
) -> Result:
    if not accumulated_results:
        accumulated_results = [Result(price=0, weight=0, items=[])]

    if len(all_items) == 0:
        max_result = accumulated_results.pop()
        for result in accumulated_results:
            if result.price > max_result.price:
                max_result = result
        return max_result

    items_left = all_items.copy()
    next_item: Item = items_left.pop()

    for result in accumulated_results.copy():
        if result.weight + next_item.weight <= capacity:
            new_result = Result(
                price=result.price + next_item.price,
                weight=result.weight + next_item.weight,
                items=[*result.items, next_item],
            )
            accumulated_results.append(new_result)

    if next_item.weight <= capacity:
        single_item_res = Result(
            price=next_item.price, weight=next_item.price, items=[next_item]
        )
        accumulated_results.append(single_item_res)

    return recursion_bf(items_left, capacity, accumulated_results)


# ==== Brute force stateless recursion


def recursion_bf_stateless(
    all_items: list[Item], capacity, pointer: Optional[int] = None
) -> Result:

    if len(all_items) == 0:
        return Result(price=0, weight=0, items=[])

    if pointer is None:
        pointer = len(all_items) - 1

    result: Result

    if pointer < 0 or capacity == 0:
        result = Result(price=0, weight=0, items=[])

    elif all_items[pointer].weight > capacity:
        result = recursion_bf_stateless(all_items, capacity, pointer - 1)

    else:
        new_item = all_items[pointer]
        with_item = add_item(
            result=recursion_bf_stateless(
                all_items, capacity - new_item.weight, pointer - 1
            ),
            item=new_item,
        )
        without_item = recursion_bf_stateless(all_items, capacity, pointer - 1)

        result = with_item if with_item.price > without_item.price else without_item

    return result


def add_item(result: Result, item: Item) -> Result:
    return Result(
        price=result.price + item.price,
        weight=0,
        items=[*result.items, item],
    )


# ==== Memoization

collector_memo: list[list[Result]] = [[]]


def recursion_bf_stateless_memo(
        all_items: list[Item], capacity, pointer: Optional[int] = None
) -> Result:
    global collector_memo  # noqa: PLW0603

    if len(all_items) == 0:
        return Result(price=0, weight=0, items=[])

    if pointer is None:
        pointer = len(all_items) - 1
        collector_memo = [[None]*(capacity + 1) for _ in range(pointer + 1)]

    if collector_memo[pointer][capacity] is not None:
        return collector_memo[pointer][capacity]

    result: Result

    if pointer < 0 or capacity == 0:
        result = Result(price=0, weight=0, items=[])

    elif all_items[pointer].weight > capacity:
        result = recursion_bf_stateless(all_items, capacity, pointer - 1)

    else:
        new_item = all_items[pointer]
        with_item = add_item(
                result=recursion_bf_stateless(
                    all_items, capacity - new_item.weight, pointer - 1
                ),
                item=new_item,
            )
        without_item = recursion_bf_stateless(all_items, capacity, pointer - 1)

        result = with_item if with_item.price > without_item.price else without_item

    collector_memo[pointer][capacity] = result
    return result


# ==== Tabulation


def knapsack_tabulation(all_items: list[Item], capacity) -> Result:
    # From https://www.w3schools.com/dsa/dsa_ref_knapsack.php
    problem_size = len(all_items)
    tab = [[0] * (capacity + 1) for _ in range(problem_size + 1)]

    for ix in range(1, problem_size + 1):
        next_item = all_items[ix-1]
        for weight in range(1, capacity + 1):
            if next_item.weight <= weight:
                include_item = next_item.price + tab[ix-1][weight - next_item.weight]
                exclude_item = tab[ix-1][weight]
                tab[ix][weight] = max(include_item, exclude_item)
            else:
                tab[ix][weight] = tab[ix-1][weight]

    items_included: list[Item] = []
    weight = capacity
    for ix in range(problem_size, 0, -1):
        if tab[ix][weight] != tab[ix-1][weight]:
            items_included.append(all_items[ix-1])
            weight -= all_items[ix-1].weight

    return Result(price=tab[problem_size][capacity], weight=0, items=items_included)


def test_no_items():
    result = loop_bf(NO_ITEMS, 10)
    assert result.price == 0
    assert len(result.items) == 0

    result = recursion_bf(NO_ITEMS, 10)
    assert result.price == 0
    assert len(result.items) == 0

    result = recursion_bf_stateless(NO_ITEMS, 10)
    assert result.price == 0
    assert len(result.items) == 0

    result = recursion_bf_stateless_memo(NO_ITEMS, 10)
    assert result.price == 0
    assert len(result.items) == 0

    result = knapsack_tabulation(NO_ITEMS, 10)
    assert result.price == 0
    assert len(result.items) == 0


def test_under_capacity():
    result = loop_bf(THREE_ITEMS, 10)
    assert result.price == 13
    assert len(result.items) == 3

    result = recursion_bf(THREE_ITEMS, 10)
    assert result.price == 13
    assert len(result.items) == 3

    result = recursion_bf_stateless(THREE_ITEMS, 10)
    assert result.price == 13
    assert len(result.items) == 3

    result = recursion_bf_stateless_memo(THREE_ITEMS, 10)
    assert result.price == 13
    assert len(result.items) == 3

    result = knapsack_tabulation(THREE_ITEMS, 10)
    assert result.price == 13
    assert len(result.items) == 3


def test_w3c():
    result = loop_bf(W3C_ITEMS, 10)
    assert result.price == 1200
    assert len(result.items) == 3

    result = recursion_bf(W3C_ITEMS, 10)
    assert result.price == 1200
    assert len(result.items) == 3

    result = recursion_bf_stateless(W3C_ITEMS, 10)
    assert result.price == 1200
    assert len(result.items) == 3

    result = recursion_bf_stateless_memo(W3C_ITEMS, 10)
    assert result.price == 1200
    assert len(result.items) == 3

    result = knapsack_tabulation(W3C_ITEMS, 10)
    assert result.price == 1200
    assert len(result.items) == 3


def test_extra_huge_items():
    result = loop_bf(HUGE_ITEMS, 10)
    assert result.price == 500
    assert len(result.items) == 2

    result = recursion_bf(HUGE_ITEMS, 10)
    assert result.price == 500
    assert len(result.items) == 2

    result = recursion_bf_stateless(HUGE_ITEMS, 10)
    assert result.price == 500
    assert len(result.items) == 2

    result = recursion_bf_stateless_memo(HUGE_ITEMS, 10)
    assert result.price == 500
    assert len(result.items) == 2

    result = knapsack_tabulation(HUGE_ITEMS, 10)
    assert result.price == 500
    assert len(result.items) == 2


def test_bigger_list():
    result = loop_bf(MANY_ITEMS, 5)
    assert result.price == 160
    assert len(result.items) == 2

    result = recursion_bf(MANY_ITEMS, 5)
    assert result.price == 160
    assert len(result.items) == 2

    result = recursion_bf_stateless(MANY_ITEMS, 5)
    assert result.price == 160
    assert len(result.items) == 2

    result = recursion_bf_stateless_memo(MANY_ITEMS, 5)
    assert result.price == 160
    assert len(result.items) == 2

    result = knapsack_tabulation(MANY_ITEMS, 5)
    assert result.price == 160
    assert len(result.items) == 2


def test_timing():
    times = 500

    print(f"\nBrute force loop {times} times")
    average = measure_the_average(loop_bf, MANY_ITEMS, 5, times)
    print(f"Average time is {average}")

    print(f"\nBrute force recursion {times} times")
    average = measure_the_average(recursion_bf, MANY_ITEMS, 5, times)
    print(f"Average time is {average}")

    print(f"\nBrute force stateless recursion {times} times")
    average = measure_the_average(recursion_bf_stateless, MANY_ITEMS, 5, times)
    print(f"Average time is {average}")

    print(f"\nStateless recursion with memoization {times} times")
    average = measure_the_average(recursion_bf_stateless_memo, MANY_ITEMS, 5, times)
    print(f"Average time is {average}")

    print(f"\nTabulation Approach {times} times")
    average = measure_the_average(knapsack_tabulation, MANY_ITEMS, 5, times)
    print(f"Average time is {average}")


def measure_the_average(func, some_list: list, capacity: int, times: int):
    stmt = f"{func.__name__}({some_list.copy()}, {capacity})"
    total_time = timeit(stmt=stmt, number=times, globals=globals())
    return f"{((total_time / times) * 1000):.6f}"
