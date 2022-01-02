def base_example_method():
    print("<base example method>\n")
    arg_1 = "value_1"
    arg_2 = "value_2"
    arg_3 = "value_3"
    arg_4 = "value_4"
    arg_5 = "value_5"

    base_example_sub_method(arg_1, arg_2, arg_3, arg_4, arg_5)


def base_example_sub_method(arg_1, arg_2, arg_3, arg_4, arg_5):
    print("<base example sub method>")
    print("drop arg_1, update arg_2 and add arg_6\n")

    arg_2 += " extra"
    arg_6 = "value_6"

    base_example_target_method(arg_2, arg_3, arg_4, arg_5, arg_6)


def base_example_target_method(arg_2, arg_3, arg_4, arg_5, arg_6):
    print("<base example target method>")
    print(f"<arg_2>='{arg_2}', <arg_3>='{arg_3}', <arg_4>='{arg_4}', "
          f"<arg_5>='{arg_5}', <arg_6>='{arg_6}'")


if __name__ == '__main__':
    base_example_method()
