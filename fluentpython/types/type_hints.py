"""
Explore type hints
Based on Fluent Python 2nd addition, Ch.13. Interfaces, Protocols, and ABCs
"""
import random
from typing import TypeVar, Protocol, Union, List, Any


class SupportsMul:
    def __mul__(self, other):
        return "__mull__() method was called"


class HasSeveralMethods:
    def method_one(self):
        print("method_one() was called")

    def method_two(self):
        print("method_two() was called")


def double_number(number):
    """Multiply given number by 2

    :param number:
    :return:
    """
    print("Inside double_number()")
    return number * 2


def double_number_with_hint(number: int) -> int:
    """Multiply given number by 2

    :param number:
    :return:
    """
    print("Inside double_number_with_hint()")
    return number * 2


def when_hints_may_help(several_methods: HasSeveralMethods):
    print("Inside when_hints_may_help()")
    several_methods.method_one()
    several_methods.method_two()
    return "Hints might have helped"


T = TypeVar('T')


class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...


RT = TypeVar('RT', bound=Repeatable)


def better_double(param: RT) -> RT:
    print("inside better_double()")
    return param * 2


def returns_int_or_string() -> Union[int, str]:
    int_and_string: List[int, str] = [123, "ABBA"]
    # int_and_string: List[Any] = [123, "ABBA"]
    return random.choice(int_and_string)


if __name__ == '__main__':
    print(double_number(10))
    # print(double_number("a"))
    # print(double_number([11, 22, 33]))
    # print(double_number(SupportsMul()))
    # print(double_number_with_hint(10))
    # print(double_number_with_hint("a"))
    # print(double_number_with_hint([11, 22, 33]))
    # print(double_number_with_hint(SupportsMul()))
    # several_methods = HasSeveralMethods()
    # print(when_hints_may_help(several_methods))
    # print(better_double(10))
    # print(better_double("a"))
    # print(better_double([11, 22, 33]))
    # print(better_double(SupportsMul()))
    # print(returns_int_or_string())
