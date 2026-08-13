import random
import time


class Quiz:

    def __init__(self, questions, topic, candidate_name):

        self.questions = questions
        self.topic = topic
        self.candidate_name = candidate_name

        self.score = 0
        self.answers = []

        self.time_limit = 10

    def start_quiz(self):

        self.score = 0
        self.answers = []

        questions = self.questions.copy()

        random.shuffle(questions)

        print("\n")
        print("=" * 55)
        print(f"              {self.topic.upper()}")
        print("=" * 55)

        print(f"\nCandidate       : {self.candidate_name}")
        print(f"Total Questions : {len(questions)}")
        print(f"Time Limit      : {self.time_limit} seconds/question")

        input("\nPress Enter to start the interview...")

        for number, question in enumerate(questions, start=1):

            self.ask_question(
                question,
                number,
                len(questions)
            )

        self.show_result()

    def ask_question(self, question, number, total):

        print("\n")
        print("-" * 55)
        print(f"Question {number} of {total}")
        print("-" * 55)

        print(question["question"])

        print()

        for index, option in enumerate(question["options"]):

            letter = chr(65 + index)

            print(f"{letter}. {option}")

        print()

        print(f"You have {self.time_limit} seconds.")

        start_time = time.time()

        answer = input(
            "Your answer (A/B/C/D): "
        ).strip().upper()

        elapsed_time = time.time() - start_time

        if elapsed_time > self.time_limit:

            print("\nTIME'S UP!")

            selected_answer = "TIMEOUT"
            is_correct = False

        elif answer not in ["A", "B", "C", "D"]:

            print("\nInvalid answer!")

            selected_answer = answer
            is_correct = False

        else:

            selected_answer = answer

            correct_answer = question["answer"].upper()

            if answer == correct_answer:

                print("\nCorrect!")

                self.score += 1
                is_correct = True

            else:

                print("\nIncorrect!")

                print(
                    f"Correct answer: {correct_answer}"
                )

                is_correct = False

        self.answers.append(
            {
                "question": question["question"],
                "selected": selected_answer,
                "correct": question["answer"],
                "is_correct": is_correct
            }
        )

        time.sleep(0.5)

    def show_result(self):

        total = len(self.questions)

        if total == 0:

            percentage = 0

        else:

            percentage = (
                self.score / total
            ) * 100

        if percentage >= 90:

            grade = "A+"
            performance = "Excellent"

        elif percentage >= 80:

            grade = "A"
            performance = "Very Good"

        elif percentage >= 70:

            grade = "B"
            performance = "Good"

        elif percentage >= 60:

            grade = "C"
            performance = "Average"

        elif percentage >= 50:

            grade = "D"
            performance = "Needs Improvement"

        else:

            grade = "F"
            performance = "Poor"

        print("\n")
        print("=" * 55)
        print("                 QUIZ RESULT")
        print("=" * 55)

        print(f"Candidate   : {self.candidate_name}")
        print(f"Topic       : {self.topic}")
        print(f"Score       : {self.score}/{total}")
        print(f"Percentage  : {percentage:.2f}%")
        print(f"Grade       : {grade}")
        print(f"Performance : {performance}")

        print("=" * 55)

        self.save_result(
            total,
            percentage,
            grade,
            performance
        )

        self.show_review()

        self.retry_menu()

    def save_result(
        self,
        total,
        percentage,
        grade,
        performance
    ):

        try:

            with open("results.txt", "a") as file:

                file.write(
                    f"Candidate: {self.candidate_name} | "
                    f"Topic: {self.topic} | "
                    f"Score: {self.score}/{total} | "
                    f"Percentage: {percentage:.2f}% | "
                    f"Grade: {grade} | "
                    f"Performance: {performance}\n"
                )

        except Exception as error:

            print(f"\nUnable to save result: {error}")

    def show_review(self):

        print("\n")
        print("=" * 55)
        print("                QUESTION REVIEW")
        print("=" * 55)

        for number, answer in enumerate(
            self.answers,
            start=1
        ):

            print()

            print(
                f"{number}. {answer['question']}"
            )

            print(
                f"Your answer    : {answer['selected']}"
            )

            print(
                f"Correct answer : {answer['correct']}"
            )

            if answer["is_correct"]:

                print("Result         : Correct")

            else:

                print("Result         : Incorrect")

        print()
        print("=" * 55)

    def retry_menu(self):

        while True:

            print("\n")
            print("=" * 55)
            print("                  WHAT NEXT?")
            print("=" * 55)

            print("1. Retry Quiz")
            print("2. Return to Main Menu")

            print("=" * 55)

            choice = input(
                "\nEnter your choice: "
            ).strip()

            if choice == "1":

                print("\nStarting quiz again...")

                self.start_quiz()

                return

            elif choice == "2":

                print(
                    "\nReturning to main menu..."
                )

                return

            else:

                print(
                    "\nInvalid choice. "
                    "Please enter 1 or 2."
                )