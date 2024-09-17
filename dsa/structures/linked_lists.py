from typing import Any, Optional

from dsa.sort_arrays.quick_sort import call_quick_sort


class Node:
    def __init__(self, value: Any):
        self.value: Any = value
        self.next: Optional["Node"] = None

    def insert(self, value: Any) -> "Node":
        pointer: "Node" = self
        while pointer.next:
            pointer = pointer.next

        new_next = Node(value)
        pointer.next = new_next

        return self

    def traverse(self) -> list[Any]:
        pointer = self
        result = [pointer.value]

        while pointer.next:
            pointer = pointer.next
            result.append(pointer.value)

        return result

    def with_removed(self, value) -> Optional["Node"]:
        pointer = self

        if pointer.value == value:
            return pointer.next

        while pointer.next:
            if pointer.next.value == value:
                pointer.next = pointer.next.next
                return self
            else:
                pointer = pointer.next

        return self

    def sort(self) -> "Node":
        sorted = call_quick_sort(self.traverse())

        pointer = self

        for value in sorted:
            pointer.value = value
            pointer = pointer.next

        return self


def test_single_node():
    test_value = 42
    linked_list = Node(test_value)

    assert linked_list.traverse() == [test_value]
    assert linked_list.with_removed(test_value) is None


def test_multiple_nodes():
    first = 202
    second = 2
    pre_last = 42
    last = 99
    linked_list = Node(first).insert(second).insert(pre_last).insert(last)

    assert linked_list.traverse() == [first, second, pre_last, last]
    linked_list = linked_list.with_removed(pre_last)
    assert linked_list.traverse() == [first, second, last]
    assert linked_list.sort().traverse() == [second, last, first]
    linked_list = linked_list.with_removed(linked_list.value)
    assert linked_list.traverse() == [last, first]
