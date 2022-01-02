def args_example_method():
    print("<base example method>\n")
    arg_1 = "value_1"
    arg_2 = "value_2"
    arg_3 = "value_3"
    arg_4 = "value_4"
    arg_5 = "value_5"

    args_example_sub_method(arg_1, arg_2, arg_3, arg_4, arg_5)


def args_example_sub_method(*args):
    print("<base example sub method>")
    new_args = list(args)

    print("drop arg_1, update arg_2 and add arg_6\n")
    new_args.pop(0)
    new_args[0] += " extra"
    new_args.insert(len(new_args), "value_6")

    args_example_target_method(*new_args)


def args_example_target_method(arg_2, arg_3, *args):
    print("<base example target method>")
    print(f"<arg_2>='{arg_2}', <arg_3>='{arg_3}', <arg_4>='{args[0]}', "
          f"<arg_5>='{args[1]}', <arg_6>='{args[2]}'")


if __name__ == '__main__':
    args_example_method()
