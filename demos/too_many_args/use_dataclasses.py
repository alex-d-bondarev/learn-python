from dataclasses import dataclass
from typing import Optional


@dataclass
class ExampleDataClass:
    arg_1: Optional[str]
    arg_2: str
    arg_3: str
    arg_4: str
    arg_5: str
    arg_6: Optional[str]


def dataclass_example_method():
    print("<base example method>\n")
    data_c = ExampleDataClass(
        arg_1="value_1",
        arg_2="value_2",
        arg_3="value_3",
        arg_4="value_4",
        arg_5="value_5",
        arg_6=None,
    )
    dataclass_example_sub_method(data_c)


def dataclass_example_sub_method(data_c):
    print("<base example sub method>")
    print("drop arg_1, update arg_2 and add arg_6\n")
    data_c.arg_1 = None
    data_c.arg_2 += " extra"
    data_c.arg_6 = "value_6"

    dataclass_example_target_method(data_c)


def dataclass_example_target_method(popo):
    print("<base example target method>")
    print(f"<arg_2>='{popo.arg_2}', <arg_3>='{popo.arg_3}', <arg_4>='{popo.arg_4}', "
          f"<arg_5>='{popo.arg_5}', <arg_6>='{popo.arg_6}'")


if __name__ == '__main__':
    dataclass_example_method()
