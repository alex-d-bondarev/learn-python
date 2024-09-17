from typing import Any


class MyStack:
    def __init__(self):
        self.values = list()

    def push(self, value: Any) -> None:
        self.values.append(value)

    def pop(self) -> Any:
        if self.is_empty():
            return None
        return self.values.pop()

    def peek(self) -> Any:
        if self.is_empty():
            return None
        return self.values[self.size() - 1]

    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return len(self.values)


def test_empty_stack():
    my_stack = MyStack()
    assert my_stack.peek() is None, "Nothing to peep() from empty stack"
    assert my_stack.is_empty() is True, "Stack is empty, so expect True"
    assert my_stack.size() == 0, "Stack is empty, so expect 0"
    assert my_stack.pop() is None, "Nothing to pop() from empty stack"


def test_single_element_stack():
    test_value = 42
    my_stack = MyStack()
    my_stack.push(test_value)

    assert my_stack.peek() == test_value, f"peek() should return {test_value}"
    assert my_stack.is_empty() is False, "Stack is not empty, so expect False"
    assert my_stack.size() == 1, "Expected stack size is 1"
    assert my_stack.pop() is test_value, f"pop() should return {test_value}"
    assert my_stack.size() == 0, "Stack is empty, after pop()"


def test_multi_element_stack():
    first = 1
    second = 2
    pre_last = 42
    last = 99

    my_stack = MyStack()
    my_stack.push(first)
    my_stack.push(second)
    my_stack.push(pre_last)
    my_stack.push(last)

    assert my_stack.peek() == last, f"peek() should return {last}"
    assert my_stack.is_empty() is False, "Stack is not empty, so expect False"
    assert my_stack.size() == 4, "Expected stack size is 4"
    assert my_stack.pop() is last, f"pop() should return {last}"
    assert my_stack.size() == 3, "Stack size is 3, after pop()"
    assert my_stack.peek() == pre_last, f"peek() should return {pre_last}"
