import random
from datetime import datetime


class Quiz:

    def __init__(self, questions, topic, name):
        self.questions = questions
        self.topic = topic
        self.name = name
        self.score = 0

    def start_quiz(self):

        if not self.questions:
            print("\nNo questions available.")
            return

        quiz_questions = self.questions.copy()

        random.shuffle(quiz_questions)

        self.score = 0

        print("\n")
        print("==================================================")
        print(f"              {self.topic.upper()} INTERVIEW")
        print("==================================================")

        print(f"Candidate : {self.name}")
        print(f"Total Questions : {len(quiz_questions)}")
        print()

        total_questions = len(quiz_questions)

        for number, question in enumerate(quiz_questions, start=1):

            progress = (number / total_questions) * 100

            print("--------------------------------------------------")
            print(f"QUESTION {number} OF {total_questions}")
            print(f"Progress: {progress:.0f}%")
            print("--------------------------------------------------")

            print(question["question"])
            print()

            for option in question["options"]:
                print(option)

            print()

            answer = input(
                "Enter your answer (A/B/C/D): "
            ).strip().upper()

            while answer not in ["A", "B", "C", "D"]:

                print("\nInvalid answer.")

                answer = input(
                    "Please enter A, B, C, or D: "
                ).strip().upper()

            if answer == question["answer"]:

                print("Correct! ✅")
                self.score += 1

            else:

                print("Wrong! ❌")

                print(
                    f"Correct answer: "
                    f"{question['answer']}"
                )

            print()

        self.show_result(total_questions)

    def show_result(self, total_questions):

        percentage = (
            self.score / total_questions
        ) * 100

        print("\n")
        print("==================================================")
        print("                 QUIZ RESULT")
        print("==================================================")

        print(f"Candidate  : {self.name}")
        print(f"Topic      : {self.topic}")
        print(
            f"Score      : "
            f"{self.score}/{total_questions}"
        )

        print(
            f"Percentage : "
            f"{percentage:.2f}%"
        )

        print("--------------------------------------------------")

        if percentage >= 80:

            print("Performance : Excellent! 🏆")

        elif percentage >= 60:

            print("Performance : Good! 👍")

        elif percentage >= 40:

            print("Performance : Needs Improvement 📚")

        else:

            print("Performance : Keep Practicing! 💪")

        print("==================================================")

        self.save_result(
            total_questions,
            percentage
        )

        print("\nResult saved successfully! 💾")

        input(
            "\nPress Enter to return to "
            "the main menu..."
        )

    def save_result(self, total_questions, percentage):

        current_time = datetime.now()

        date_time = current_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        result = (
            f"{date_time} | "
            f"Candidate: {self.name} | "
            f"Topic: {self.topic} | "
            f"Score: {self.score}/"
            f"{total_questions} | "
            f"Percentage: {percentage:.2f}%\n"
        )

        with open("results.txt", "a") as file:
            file.write(result)