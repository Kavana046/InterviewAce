class PerformanceAnalyzer:
    """
    Handles score calculation and performance evaluation
    for InterviewAce.
    """

    def __init__(self, score, total_questions):
        self.score = score
        self.total_questions = total_questions

    # ==========================================
    # CALCULATE PERCENTAGE
    # ==========================================

    def calculate_percentage(self):
        if self.total_questions == 0:
            return 0.0

        return (
            self.score / self.total_questions
        ) * 100

    # ==========================================
    # CALCULATE CORRECT ANSWERS
    # ==========================================

    def get_correct_answers(self):
        return self.score

    # ==========================================
    # CALCULATE WRONG ANSWERS
    # ==========================================

    def get_wrong_answers(self):
        return (
            self.total_questions - self.score
        )

    # ==========================================
    # GET GRADE
    # ==========================================

    def get_grade(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 60:
            return "C"

        elif percentage >= 50:
            return "D"

        else:
            return "F"

    # ==========================================
    # GET PERFORMANCE
    # ==========================================

    def get_performance(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "Excellent"

        elif percentage >= 80:
            return "Very Good"

        elif percentage >= 70:
            return "Good"

        elif percentage >= 60:
            return "Average"

        elif percentage >= 50:
            return "Needs Improvement"

        else:
            return "Poor"

    # ==========================================
    # GET COMPLETE ANALYSIS
    # ==========================================

    def get_analysis(self):

        percentage = self.calculate_percentage()

        correct = self.get_correct_answers()

        wrong = self.get_wrong_answers()

        grade = self.get_grade()

        performance = self.get_performance()

        return {
            "score": self.score,
            "total": self.total_questions,
            "correct": correct,
            "wrong": wrong,
            "percentage": percentage,
            "grade": grade,
            "performance": performance
        }


# ==============================================
# TEST
# ==============================================

if __name__ == "__main__":

    analyzer = PerformanceAnalyzer(
        8,
        10
    )

    result = analyzer.get_analysis()

    print("Performance Analysis")
    print("--------------------")

    print(
        f"Score       : "
        f"{result['score']}/{result['total']}"
    )

    print(
        f"Correct     : "
        f"{result['correct']}"
    )

    print(
        f"Wrong       : "
        f"{result['wrong']}"
    )

    print(
        f"Percentage  : "
        f"{result['percentage']:.2f}%"
    )

    print(
        f"Grade       : "
        f"{result['grade']}"
    )

    print(
        f"Performance : "
        f"{result['performance']}"
    )