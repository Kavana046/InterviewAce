from quiz import Quiz
from questions import (
    python_questions,
    git_questions,
    linux_questions
)


def show_menu():

    print("\n")
    print("=" * 55)
    print("                  INTERVIEWACE")
    print("=" * 55)

    print("1. Python Interview")
    print("2. Git Interview")
    print("3. Linux Interview")
    print("4. View Previous Results")
    print("5. Clear Previous Results")
    print("6. About InterviewAce")
    print("7. View Leaderboard")
    print("8. Help / Instructions")
    print("9. Question Bank Statistics")
    print("10. Exit")

    print("=" * 55)


def show_difficulty_menu():

    print("\n")
    print("-" * 55)
    print("              SELECT DIFFICULTY")
    print("-" * 55)

    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Back to Main Menu")

    print("-" * 55)


def select_difficulty(questions, topic, name):

    while True:

        show_difficulty_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            difficulty = "Easy"

        elif choice == "2":

            difficulty = "Medium"

        elif choice == "3":

            difficulty = "Hard"

        elif choice == "4":

            return

        else:

            print(
                "\nInvalid choice."
            )

            continue

        selected_questions = [
            question
            for question in questions
            if question["difficulty"] == difficulty
        ]

        if not selected_questions:

            print(
                f"\nNo {difficulty} questions available."
            )

            continue

        quiz = Quiz(
            selected_questions,
            f"{topic} - {difficulty}",
            name
        )

        quiz.start_quiz()


def show_results():

    print("\n")
    print("=" * 55)
    print("                PREVIOUS RESULTS")
    print("=" * 55)

    try:

        with open("results.txt", "r") as file:

            results = file.readlines()

    except FileNotFoundError:

        results = []

    valid_results = [
        result.strip()
        for result in results
        if result.strip()
    ]

    if not valid_results:

        print("\nNo previous results available.")

        print(
            "Complete an interview first "
            "to see your results."
        )

        print("=" * 55)

        input(
            "\nPress Enter to return to the main menu..."
        )

        return

    for number, result in enumerate(
        valid_results,
        start=1
    ):

        parts = result.split(" | ")

        candidate = "Unknown"
        topic = "Unknown"
        score = "0/0"
        percentage = "0%"
        grade = "F"
        performance = "Unknown"

        for part in parts:

            if part.startswith("Candidate:"):

                candidate = part.replace(
                    "Candidate:",
                    ""
                ).strip()

            elif part.startswith("Topic:"):

                topic = part.replace(
                    "Topic:",
                    ""
                ).strip()

            elif part.startswith("Score:"):

                score = part.replace(
                    "Score:",
                    ""
                ).strip()

            elif part.startswith("Percentage:"):

                percentage = part.replace(
                    "Percentage:",
                    ""
                ).strip()

            elif part.startswith("Grade:"):

                grade = part.replace(
                    "Grade:",
                    ""
                ).strip()

            elif part.startswith("Performance:"):

                performance = part.replace(
                    "Performance:",
                    ""
                ).strip()

        print()
        print(f"---------------- ATTEMPT {number} ----------------")

        print(f"Candidate   : {candidate}")
        print(f"Topic       : {topic}")
        print(f"Score       : {score}")
        print(f"Percentage  : {percentage}")
        print(f"Grade       : {grade}")
        print(f"Performance : {performance}")

        print("-" * 55)

    print(
        f"\nTotal Attempts: {len(valid_results)}"
    )

    print("=" * 55)

    input(
        "\nPress Enter to return to the main menu..."
    )


def clear_results():

    print("\n")
    print("=" * 55)
    print("              CLEAR PREVIOUS RESULTS")
    print("=" * 55)

    confirmation = input(
        "\nAre you sure you want to clear all results? "
        "(yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        with open("results.txt", "w") as file:

            file.write("")

        print(
            "\nAll previous results have been cleared."
        )

    else:

        print(
            "\nResults were not deleted."
        )

    input(
        "\nPress Enter to return to the main menu..."
    )


def show_about():

    print("\n")
    print("=" * 55)
    print("                ABOUT INTERVIEWACE")
    print("=" * 55)

    print()
    print(
        "InterviewAce is a command-line interview "
        "preparation application developed using Python."
    )

    print()
    print("Technical Domains:")
    print("• Python")
    print("• Git")
    print("• Linux")

    print()
    print("Features:")
    print("• Interactive interview quizzes")
    print("• Multiple difficulty levels")
    print("• Randomized questions")
    print("• Timed questions")
    print("• Automatic score calculation")
    print("• Grade and performance evaluation")
    print("• Previous result tracking")
    print("• Question review")
    print("• Quiz retry")
    print("• Leaderboard")
    print("• Question bank statistics")

    print()
    print("Technologies:")
    print("• Python")
    print("• Object-Oriented Programming")
    print("• Git")
    print("• GitHub")

    print()
    print("=" * 55)

    input(
        "\nPress Enter to return to the main menu..."
    )


def show_leaderboard():

    print("\n")
    print("=" * 70)
    print("                         LEADERBOARD")
    print("=" * 70)

    try:

        with open("results.txt", "r") as file:

            results = file.readlines()

    except FileNotFoundError:

        results = []

    leaderboard = []

    for result in results:

        result = result.strip()

        if not result:
            continue

        parts = result.split(" | ")

        candidate = "Unknown"
        topic = "Unknown"
        score = "0/0"
        percentage = 0.0
        grade = "F"

        for part in parts:

            if part.startswith("Candidate:"):

                candidate = part.replace(
                    "Candidate:",
                    ""
                ).strip()

            elif part.startswith("Topic:"):

                topic = part.replace(
                    "Topic:",
                    ""
                ).strip()

            elif part.startswith("Score:"):

                score = part.replace(
                    "Score:",
                    ""
                ).strip()

            elif part.startswith("Percentage:"):

                percentage_text = part.replace(
                    "Percentage:",
                    ""
                ).replace(
                    "%",
                    ""
                ).strip()

                try:

                    percentage = float(
                        percentage_text
                    )

                except ValueError:

                    percentage = 0.0

            elif part.startswith("Grade:"):

                grade = part.replace(
                    "Grade:",
                    ""
                ).strip()

        leaderboard.append(
            {
                "candidate": candidate,
                "topic": topic,
                "score": score,
                "percentage": percentage,
                "grade": grade
            }
        )

    if not leaderboard:

        print("\nNo scores available yet.")

        print("=" * 70)

        input(
            "\nPress Enter to return to the main menu..."
        )

        return

    leaderboard.sort(
        key=lambda item: item["percentage"],
        reverse=True
    )

    print()

    print(
        f"{'Rank':<8}"
        f"{'Candidate':<18}"
        f"{'Topic':<22}"
        f"{'Score':<10}"
        f"{'Percentage':<12}"
        f"{'Grade'}"
    )

    print("-" * 70)

    for position, entry in enumerate(
        leaderboard[:10],
        start=1
    ):

        print(
            f"{position:<8}"
            f"{entry['candidate'][:17]:<18}"
            f"{entry['topic'][:21]:<22}"
            f"{entry['score']:<10}"
            f"{entry['percentage']:.2f}%{'':<6}"
            f"{entry['grade']}"
        )

    print()
    print("=" * 70)

    input(
        "\nPress Enter to return to the main menu..."
    )


def show_help():

    print("\n")
    print("=" * 55)
    print("              INTERVIEWACE HELP")
    print("=" * 55)

    print()
    print("How to use InterviewAce:")
    print()

    print("1. Enter your name.")
    print()

    print("2. Select a technical domain:")
    print("   • Python")
    print("   • Git")
    print("   • Linux")
    print()

    print("3. Select a difficulty:")
    print("   • Easy")
    print("   • Medium")
    print("   • Hard")
    print()

    print("4. Answer each question using A, B, C or D.")
    print()

    print("5. Each question has a 10-second time limit.")
    print()

    print("6. Questions are displayed randomly.")
    print()

    print("7. At the end you receive:")
    print("   • Score")
    print("   • Percentage")
    print("   • Grade")
    print("   • Performance")
    print("   • Question review")
    print()

    print("8. Results are automatically saved.")
    print()

    print("9. Previous attempts can be viewed.")
    print()

    print("10. The leaderboard displays the highest scores.")
    print()

    print("11. Question Bank Statistics displays")
    print("    the available questions.")
    print()

    print("12. Select Exit to close InterviewAce.")

    print()
    print("=" * 55)

    input(
        "\nPress Enter to return to the main menu..."
    )


def show_question_statistics():

    topics = [
        ("Python", python_questions),
        ("Git", git_questions),
        ("Linux", linux_questions)
    ]

    print("\n")
    print("=" * 55)
    print("             QUESTION BANK STATISTICS")
    print("=" * 55)

    total_questions = 0

    for topic, questions in topics:

        easy = sum(
            1
            for question in questions
            if question["difficulty"] == "Easy"
        )

        medium = sum(
            1
            for question in questions
            if question["difficulty"] == "Medium"
        )

        hard = sum(
            1
            for question in questions
            if question["difficulty"] == "Hard"
        )

        total = easy + medium + hard

        total_questions += total

        print()
        print(topic.upper())
        print("-" * 35)

        print(f"Easy   : {easy}")
        print(f"Medium : {medium}")
        print(f"Hard   : {hard}")
        print(f"Total  : {total}")

    print()
    print("-" * 55)

    print(
        f"TOTAL QUESTIONS: {total_questions}"
    )

    print("=" * 55)

    input(
        "\nPress Enter to return to the main menu..."
    )


def main():

    print("\n")
    print("=" * 55)
    print("          WELCOME TO INTERVIEWACE")
    print("=" * 55)

    name = input(
        "\nEnter your name: "
    ).strip()

    if not name:

        name = "Candidate"

    while True:

        show_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            select_difficulty(
                python_questions,
                "Python",
                name
            )

        elif choice == "2":

            select_difficulty(
                git_questions,
                "Git",
                name
            )

        elif choice == "3":

            select_difficulty(
                linux_questions,
                "Linux",
                name
            )

        elif choice == "4":

            show_results()

        elif choice == "5":

            clear_results()

        elif choice == "6":

            show_about()

        elif choice == "7":

            show_leaderboard()

        elif choice == "8":

            show_help()

        elif choice == "9":

            show_question_statistics()

        elif choice == "10":

            confirmation = input(
                "\nAre you sure you want to exit? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":

                print()
                print("=" * 55)
                print("       Thank you for using InterviewAce!")
                print("       Keep learning and keep practicing!")
                print("=" * 55)

                break

            else:

                print(
                    "\nReturning to the main menu..."
                )

        else:

            print(
                "\nInvalid choice."
            )

            print(
                "Please select a number from 1 to 10."
            )


if __name__ == "__main__":
    main()