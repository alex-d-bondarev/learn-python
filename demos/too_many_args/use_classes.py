class ExampleClass:
    def __init__(self, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.arg_3 = arg_3
        self.arg_4 = arg_4
        self.arg_5 = arg_5
        self.arg_6 = arg_6


def class_example_method():
    print("<base example method>\n")
    popo = ExampleClass(  # Plain old python class
        arg_1="value_1",
        arg_2="value_2",
        arg_3="value_3",
        arg_4="value_4",
        arg_5="value_5",
        arg_6=None,
    )
    class_example_sub_method(popo)


def class_example_sub_method(popo):
    print("<base example sub method>")
    print("drop arg_1, update arg_2 and add arg_6\n")
    popo.arg_1 = None
    popo.arg_2 += " extra"
    popo.arg_6 = "value_6"

    class_example_target_method(popo)


def class_example_target_method(popo):
    print("<base example target method>")
    print(f"<arg_2>='{popo.arg_2}', <arg_3>='{popo.arg_3}', <arg_4>='{popo.arg_4}', "
          f"<arg_5>='{popo.arg_5}', <arg_6>='{popo.arg_6}'")


if __name__ == '__main__':
    class_example_method()
