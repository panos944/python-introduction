def test_args_func(pos_arg1, pos_arg2, opt_arg1 = None, opt_arg2 = None, *args, **kwargs):
    """
    Function to demonstrate the usage of positional, optional, additional optional(*args)

    Parameters:
        pos_arg1 (Any): The first positional argument.
        pos_arg2: The second positional argument.
        opt_arg1: The first optional argument. Defaults to none.
        opt_arg2: The second optional argument. Defaults to none.  
        *args: Additional positional arguments.
        **kwarg s: Additional keyword arguments.
    """

    # Print positional arguments
    print("Pos arg1 :", pos_arg1)
    print("Pos arg2 :", pos_arg2)

     # Print optional arguments
    print("Pos opt1 :", opt_arg1)
    print("Pos opt2 :", opt_arg2)

    # Pront addiotnal pos args
    if args:
        print("Additional pos args")
        for arg in args:
            print(args)
    
    if kwargs:
        print("Additional keyword args")
        for key, value in kwargs.items():
            print(f"{key}:{value}")
    

def main():
    test_args_func("Hello", "CF7", 100, 200)
    print("-----------")

    test_args_func("Hello", "CF7", opt_arg2=100)
    print("-----------")

    test_args_func("Hello", "CF7", name="Panagiotis", age=101)
    print("-----------")
    
    test_args_func("Helo", "CF", # pos_arg1, pos_arg2
                   100, 200,     # opt_arg1, opt_arg2
                   300, "Bob",    # args
                   name="Panos", street="Coding" #kwargs
    )


if __name__ == "__main__":
    main()