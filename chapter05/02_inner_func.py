from typing import List, Tuple, Union

def calculate_grade(assignment_scores: List[Union[int, float]], final_score: Union[int, float], mid_score: Union[int, float]) -> Tuple[float, str]:
    
    def weighted_average() -> float:
        assignment_score = sum(assignment_scores / len(assignment_scores))
        return (assignment_score * 0.4) + (mid_score * 0.3) + (final_score * 0.3)
    
    def determine_grade(average:float) -> str: 
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        else:
            return "D"
    
    average = weighted_average()
    grade = determine_grade(average)

    return average, grade

def main():
    final_average, final_grade = calculate_grade([92, 90, 100], 85, 59)
    print(f"final average: {final_average}, final_grade: {final_grade}")

if __name__ == "__main__":
    main()