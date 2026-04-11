# Credit to https://github.com/ByteQuest0/Implemention_codes/blob/main/Heaps/heap.py
from typing import Optional


class MyBinaryMaxHeap:
    def __init__(self) -> None:
        self.heap = []

    @staticmethod
    def parent(index: int) -> int:
        return (index - 1) // 2

    @staticmethod
    def left_child(index: int) -> int:
        return index * 2 + 1

    @staticmethod
    def right_child(index: int) -> int:
        return index * 2 + 2

    def heapify_up(self, index: int) -> None:
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def heapify_down(self, index: int) -> None:
        size = len(self.heap)
        largest = index

        while True:
            left = self.left_child(index)
            right = self.right_child(index)

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest
            else:
                break

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def build_heap(self, new_list) -> None:
        self.heap = new_list[:]
        # Start from the last non-leaf node and heapify down each node
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def extract_max(self) -> Optional[int]:
        if not self.heap:
            return None

        maximum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return maximum


    def get_max(self) -> Optional[int]:
        if self.heap:
            return self.heap[0]
        return None

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def clear(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)


def test_empty_heap():
    heap = MyBinaryMaxHeap()
    assert heap.get_max() is None
    assert heap.extract_max() is None
    assert heap.is_empty() == True
    assert heap.size() == 0


def test_heap_from_list_same_as_from_inserts():
    grown_heap = MyBinaryMaxHeap()
    grown_heap.insert(10)
    grown_heap.insert(5)
    grown_heap.insert(7)
    grown_heap.insert(20)
    grown_heap.insert(9)
    grown_heap.insert(15)

    built_heap = MyBinaryMaxHeap()
    built_heap.build_heap([10, 5, 7, 20, 9, 15])

    assert built_heap.heap == grown_heap.heap
    assert built_heap.heap == [20, 10, 15, 5, 9, 7]
    assert grown_heap.extract_max() == 20
    assert grown_heap.extract_max() == 15
    assert grown_heap.extract_max() == 10
    assert grown_heap.extract_max() == 9
    assert grown_heap.extract_max() == 7
    assert grown_heap.extract_max() == 5
    assert grown_heap.extract_max() is None