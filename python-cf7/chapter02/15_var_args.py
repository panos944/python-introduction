def print_cities(*cities):
    if not cities: 
        print("No cities provided")
    else:
        print("Cities:", ", ".join(cities))

def main():
    print_cities()
    print("Athens")
    print("Athens", "Paris", "London")

if __name__ == "__main__":
    main()