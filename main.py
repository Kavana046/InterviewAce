from quiz import Quiz
from questions import python_questions, git_questions, linux_questions


def show_menu():
    print("\n")
    print("==================================================")
    print("                  INTERVIEWACE")
    print("==================================================")
    print("1. Python Interview")
    print("2. Git Interview")
    print("3. Linux Interview")
    print("4. View Previous Results")
    print("5. Clear Previous Results")
    print("6. About InterviewAce")
    print("7. Exit")
    print("==================================================")


def show_difficulty_menu():
    print("\n")
    print("--------------- SELECT DIFFICULTY ----------------")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Back to Main Menu")
    print("---------------------------------------------------")


def select_difficulty(questions, topic, name):

    while True:

        show_difficulty_menu()

        difficulty_choice = input(
            "\nEnter your choice: "
        ).strip()

        if difficulty_choice == "1":

            difficulty = "Easy"

        elif difficulty_choice == "2":

            difficulty = "Medium"

        elif difficulty_choice == "3":

            difficulty = "Hard"

        elif difficulty_choice == "4":

            break

        else:

            print(
                "\nInvalid difficulty choice. "
                "Please select 1, 2, 3, or 4."
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
    print("==================================================")
    print("               PREVIOUS RESULTS")
    print("==================================================")

    try:

        with open("results.txt", "r") as file:

            results = file.read()

            if results.strip():

                print(results)

            else:

                print("\nNo previous results available.")

    except FileNotFoundError:

        print("\nNo previous results available.")

    print("==================================================")

    input(
        "\nPress Enter to return to the main menu..."
    )


def clear_results():

    print("\n")
    print("==================================================")
    print("              CLEAR PREVIOUS RESULTS")
    print("==================================================")

    confirmation = input(
        "\nAre you sure you want to clear all results? "
        "(yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        with open("results.txt", "w") as file:
            file.write("")

        print("\nAll previous results have been cleared. 🗑️")

    else:

        print("\nResults were not deleted.")

    input(
        "\nPress Enter to return to the main menu..."
    )


def show_about():

    print("\n")
    print("==================================================")
    print("                ABOUT INTERVIEWACE")
    print("==================================================")
    print()
    print(
        "InterviewAce is a command-line interview "
        "preparation application developed using Python."
    )
    print()
    print("Available Technical Domains:")
    print("• Python")
    print("• Git")
    print("• Linux")
    print()
    print("Features:")
    print("• Interactive interview quizzes")
    print("• Easy, Medium and Hard questions")
    print("• Automatic score calculation")
    print("• Performance evaluation")
    print("• Previous result tracking")
    print("• Quiz retry option")
    print("• Clear previous results")
    print()
    print("Developed using:")
    print("• Python")
    print("• Object-Oriented Programming")
    print("• Git and GitHub")
    print()
    print("==================================================")

    input(
        "\nPress Enter to return to the main menu..."
    )


def main():

    print("\n")
    print("==================================================")
    print("          WELCOME TO INTERVIEWACE 🚀")
    print("==================================================")

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

            print(
                "\nThank you for using InterviewAce! 🎯"
            )

            print(
                "Keep learning and keep practicing! 🚀"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1, 2, 3, 4, 5, 6, or 7."
            )


if __name__ == "__main__":
    main()