def is_square(length: int, width: int) -> bool:
    """
    Checks if a rectangle is a square. 

    Args:
        length(int): The length of the rectangle. 

    Returns: 
        bool: True of the rectangle is square, False otherwise.
    """
    return length == width

def main():
    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle"))
    except ValueError:
        print("Error - 2 digits needed.")

    if is_square(length, width):
        print("The rectangle is square")
    else:
        print("The rectangle is not square.")


if __name__ == "__main__":
    main()