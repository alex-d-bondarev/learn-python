class MyQueue:
    def __init__(self):
        self.values = list()

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.values.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.values[0]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.values)


def test_empty_queue():
    my_queue = MyQueue()

    assert my_queue.size() == 0, "Queue should be empty"
    assert my_queue.is_empty() is True, "Queue should be empty"
    assert my_queue.peek() is None, "Queue should be empty, so None value to peek()"
    assert my_queue.dequeue() is None, "Queue should be empty, so None value to dequeue()"


def test_single_value_queue():
    test_value = 42
    my_queue = MyQueue()
    my_queue.enqueue(test_value)

    assert my_queue.size() == 1, "Queue should not be empty"
    assert my_queue.is_empty() is False, "Queue should not be empty"
    assert my_queue.peek() == test_value, f"Expect peek() to return {test_value}"
    assert my_queue.dequeue() == test_value, f"Expect dequeue() to return {test_value}"
    assert my_queue.size() == 0, "Queue should be empty after dequeue()"
    assert my_queue.is_empty() is True, "Queue should be empty after dequeue()"


def test_fifo_multiple_elements():
    first = 1
    second = 2
    pre_last = 42
    last = 99

    my_queue = MyQueue()
    my_queue.enqueue(first)
    my_queue.enqueue(second)
    my_queue.enqueue(pre_last)
    my_queue.enqueue(last)

    assert my_queue.size() == 4, "Queue should not be empty"
    assert my_queue.is_empty() is False, "Queue should not be empty"
    assert my_queue.peek() == first, f"Expect peek() to return {first}"
    assert my_queue.dequeue() == first, f"Expect dequeue() to return {first}"
    assert my_queue.size() == 3, f"Expect queue size to reduce by 1 after dequeue() and become 3"
    assert my_queue.peek() == second, f"Expect peek() to return {second} after dequeue()"
