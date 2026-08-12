from quiz import Quiz
from questions import python_questions, git_questions, linux_questions


def show_welcome():
    print("\n")
    print("==================================================")
    print("              🎯 WELCOME TO INTERVIEWACE")
    print("==================================================")
    print("       Python Interview Preparation System")
    print("==================================================")
    print()


def show_menu():
    print("\n---------------- MAIN MENU ----------------")
    print("1. Python Interview")
    print("2. Git Interview")
    print("3. Linux Interview")
    print("4. View Previous Results")
    print("5. Exit")
    print("-------------------------------------------")


def select_difficulty(questions, topic, name):

    while True:

        print("\n----------- SELECT DIFFICULTY -----------")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Back to Main Menu")
        print("-----------------------------------------")

        difficulty_choice = input(
            "Enter your choice: "
        ).strip()

        if difficulty_choice == "4":
            return

        if difficulty_choice == "1":
            difficulty = "Easy"

        elif difficulty_choice == "2":
            difficulty = "Medium"

        elif difficulty_choice == "3":
            difficulty = "Hard"

        else:
            print("\nInvalid difficulty choice.")
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
            topic,
            name
        )

        quiz.start_quiz()

        return


def view_results():

    print("\n")
    print("==================================================")
    print("                 📊 PREVIOUS RESULTS")
    print("==================================================")

    try:

        with open("results.txt", "r") as file:
            results = file.read()

        if results.strip():

            print(results)

        else:

            print("\nNo results available yet.")

    except FileNotFoundError:

        print("\nNo results available yet.")

    print("==================================================")

    input(
        "\nPress Enter to return to the main menu..."
    )


def main():

    show_welcome()

    name = input(
        "Enter your name: "
    ).strip()

    if not name:
        name = "Candidate"

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
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

            view_results()

        elif choice == "5":

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
                "Please select 1, 2, 3, 4, or 5."
            )


if __name__ == "__main__":
    main()