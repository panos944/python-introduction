class Student: 
    """
    A class that represents a student with a first name and a a last name.

    Attrs:
    firstname(str): The first name of the student.
    lastname(str): The last name of the student.
    """

    def __init__(self, firstname: str, lastname: str):
        """..."""
        self.firstname = firstname
        self.lastname = lastname
        pass
    
def main():
    st = Student("Bob", "M.")
    print(f"First name: {st.firstname}")
    print(f"Last name: {st.lastname}")


if __name__ == "__main__":
    main()