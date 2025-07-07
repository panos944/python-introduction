def get_average(*numbers):
    pass

    if not numbers:
        return "No numbers provided."
    
    average = sum(numbers) / len(numbers)
    
    return"{:.2f}".format(average)

def main():
    nums = [10, 20, 30, 40]

    my_average = get_average(*nums)

    print(my_average)

if __name__ == "__main__":
    main()