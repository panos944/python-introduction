def my_add(a: float | int, b: float | int):
    """
    Adds two numbers and returns the result. 

    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add.

    Returns:
        int | float: The sum of "a" and "b"

    Raise: 
        TypeError: If either 'a' or 'b' is not an integer or float.  
    """
    if not (isinstance(a, (int,float)) and isinstance(b, (int, float))):
        raise TypeError("Both a and b must be integers.")
    return a + b

def main():
    print(my_add(10, 20.5))

    try:
        print(my_add("Hello", 10))
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()