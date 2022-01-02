from collections import namedtuple

ExampleNamedTuple = namedtuple("ExampleNamedTuple",
                               "arg_1 arg_2 arg_3 arg_4 arg_5 arg_6")


def namedtuple_example_method():
    print("<base example method>\n")
    dto = ExampleNamedTuple(  # Data transfer object
        arg_1="value_1",
        arg_2="value_2",
        arg_3="value_3",
        arg_4="value_4",
        arg_5="value_5",
        arg_6=None,
    )
    namedtuple_example_sub_method(dto)


def namedtuple_example_sub_method(dto):
    print("<base example sub method>")
    print("drop arg_1, update arg_2 and add arg_6\n")
    new_dto = ExampleNamedTuple(
        arg_1=None,
        arg_2=dto.arg_2 + " extra",
        arg_3=dto.arg_3,
        arg_4=dto.arg_4,
        arg_5=dto.arg_6,
        arg_6="value_6",
    )

    namedtuple_example_target_method(new_dto)


def namedtuple_example_target_method(dto):
    print("<base example target method>")
    print(f"<arg_2>='{dto.arg_2}', <arg_3>='{dto.arg_3}', <arg_4>='{dto.arg_4}', "
          f"<arg_5>='{dto.arg_5}', <arg_6>='{dto.arg_6}'")


if __name__ == '__main__':
    namedtuple_example_method()
