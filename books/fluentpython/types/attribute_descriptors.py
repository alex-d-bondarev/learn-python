"""
Explore type, instance and attribute descriptors
Based on Fluent Python 2nd addition, Ch.23. Attribute Descriptors
"""


class ParentClass:
    def explain(self):
        return "it's the ParentClass"


class ChildClass(ParentClass):
    def explain(self):
        return "it's the ChildClass"


class SubChildClass(ChildClass):
    def explain(self):
        return "it's the SubChildClass"


parent = ParentClass()
child = ChildClass()
sub_child = SubChildClass()


def type_example():
    assert type(parent) is ParentClass, parent.explain()
    assert type(child) is ChildClass, child.explain()
    assert type(sub_child) is SubChildClass, sub_child.explain()

    assert type(child) is not ParentClass, child.explain()
    assert type(child) is not SubChildClass, child.explain()


def is_instance_example():
    assert isinstance(parent, ParentClass), parent.explain()
    assert isinstance(child, ParentClass), child.explain()
    assert isinstance(sub_child, ParentClass), sub_child.explain()

    assert not isinstance(parent, ChildClass), parent.explain()
    assert isinstance(child, ChildClass), child.explain()
    assert isinstance(sub_child, SubChildClass), sub_child.explain()


class ChildType:
    """type(value) is ChildClass"""

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if type(value) is ChildClass:
            instance.__dict__[self.name] = value
        else:
            message = f"{self.name} must be of Child class type but {value.explain()}"
            raise ValueError(message)

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class ChildInstace:
    """isinstance(value, ChildClass)"""

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if isinstance(value, ChildClass):
            instance.__dict__[self.name] = value
        else:
            message = f"{self.name} must be instance of Child class but {value.explain()}"
            raise ValueError(message)

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class TypesTest:
    child_type = ChildType("child_type")
    child_instance = ChildInstace("child_instance")

    def __init__(self, child_type, child_instance):
        self.child_type = child_type
        self.child_instance = child_instance


class NaturalSingleDigitNumber:
    """1, 2, 3, 4, 5, 6, 7, 8, 9"""

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if isinstance(value, int) \
                and 1 <= value <= 9:
            instance.__dict__[self.name] = value
        else:
            message = f"{self.name} must be 1, 2, 3, 4, 5, 6, 7, 8, or 9, but not {value}"
            raise ValueError(message)

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class TestNaturalSingleDigitNumber:
    the_number = NaturalSingleDigitNumber("the_number")

    def __init__(self, the_number):
        self.the_number = the_number


if __name__ == '__main__':
    type_example()

    # is_instance_example()

    # descriptors_are_met = TypesTest(
    #     child_type=child,
    #     child_instance=sub_child
    # )

    # descriptors_are_violated = TypesTest(
    #     child_type=child,
    #     child_instance=parent
    # )

    # natural_single_digit = TestNaturalSingleDigitNumber(5)
    # natural_single_digit_violation = TestNaturalSingleDigitNumber(-5)
