def kwargs_example_method():
    print("<base example method>\n")
    arg_1 = "value_1"
    arg_2 = "value_2"
    arg_3 = "value_3"
    arg_4 = "value_4"
    arg_5 = "value_5"

    kwargs_example_sub_method(arg_1=arg_1, arg_2=arg_2, arg_3=arg_3,
                              arg_4=arg_4, arg_5=arg_5)


def kwargs_example_sub_method(**kwargs):
    print("<base example sub method>")
    print("drop arg_1, update arg_2 and add arg_6\n")

    kwargs.pop("arg_1")
    kwargs["arg_2"] += " extra"
    kwargs["arg_6"] = "value_6"

    kwargs_example_target_method(**kwargs)


def kwargs_example_target_method(arg_2, arg_3, **kwargs):
    print("<base example target method>")
    print(f"<arg_2>='{arg_2}', <arg_3>='{arg_3}', <arg_4>='{kwargs['arg_4']}', "
          f"<arg_5>='{kwargs['arg_5']}', <arg_6>='{kwargs['arg_6']}'")


if __name__ == '__main__':
    kwargs_example_method()
