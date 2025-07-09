students = {
    'Alice': [85, 92, 78],
    'Bob': [79, 95, 88],
    'Charlie': [68, 72, 80],
    'Diana': [95, 98, 100],
    'Eve': [50, 60, 58]
}


def main():
    while True:
        try: 
            threshold = int(input("Please insert a threshold(int): "))
        except ValueError:
            print("Invalid input.")
            continue

        average_grades = {
            student: round(sum(grades) / len(grades), 2)
            for student, grades in students.items()
            if grades and (sum(grades) / len(grades)) > threshold
        }

        for student, avg_grade in average_grades.items():
            print(f"{student}: {avg_grade}")


if __name__ == "__main__":
    main()