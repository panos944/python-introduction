def print_cities(*cities, sep=", ", end="\n"):
    """
    Print a list of cities separeted by a specific separator and ending with a specified char. 

    Parameters:
        *cities (str): Cities which are going to be printed.
        sep(str): Separator between city name. Default is ",".
        end(str): End character after the last citiy. Default is "\n".
    """
    

    if not cities: 
        print("No cities provided", end=end)
    else:
        print("Cities:", sep.join(cities), end=end)

def main():
    print_cities()
    print("Athens")
    print("Athens", "Paris", "London")
    print("-----------------")

    print_cities("Athens", "Paris", "Patra", sep=" | ", end=".")
    print("\n--------------- ")

if __name__ == "__main__":
    main()