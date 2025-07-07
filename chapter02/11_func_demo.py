def say_hello(name:str = "Coding Factory"):
    """
    Print a greeting message.
    
    Args:
        name(str): The name to greet. Default value 'Coding Factory'
    """
    print(f"Hello {name}")

def main():
    # say_hello("Panos")
    say_hello()
    say_hello("Panos")
    
    # print(say_hello.__doc__)
    help(say_hello)
    pass
 
if __name__ == "__main__": 
    main()