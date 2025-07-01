import string
import random

# string to list
characters = list(string.ascii_letters + string.digits + "!&*(@&dsa")
# print(characters)

def generate_password():
    
    """
    Generates a random password based on the user's specified length
    """
    try:
        password_length = int(input("Give the password length: "))

        if password_length <= 0:
            print("Password lenth can't be negative or 0")
            return
    except ValueError:
        print("Invalid input. Please provide a positive integer")
        return
    
    random.shuffle(characters)

    password = []

    for i in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    # list to string
    password = "".join(password)

    print(f"Generate password: {password}")

def main():
    while True:
        option = input("\nDo you want to create a password? ('y' or 'q' for quit): ")

        if option.lower() == 'y':
            generate_password()
        elif option.lower == 'q': 
            print("Goodbye")
            break
        else:
            print("Wrong input")

if __name__ == "__main__":
    main()