def calculcate_sum_and_product(upper_bound):
    total_sum = 0
    total_product = 1

    for i in range(1, upper_bound + 1):
        total_sum += i
        total_product *= i

    return total_sum, total_product

def main():
    try:
        upper_bound = int(input("Please insert an integer: "))
    except ValueError:
        print("Invalid input")
        return

    total_sum, total_product = calculcate_sum_and_product(upper_bound)

    print(f"Sum(1 - {upper_bound}) = {total_sum}")
    print(f"Product(1 - {upper_bound}) = {total_product}")

if __name__ == "__main__":
    main()
