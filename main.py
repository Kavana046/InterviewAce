from quiz import Quiz
from questions import python_questions, git_questions, linux_questions


def welcome():

    print("\n")
    print("==============================================")
    print("              INTERVIEW ACE")
    print("       Python Interview Preparation")
    print("==============================================")
    print()
    print("Prepare. Practice. Perform.")
    print()
    print("Technical Domains:")
    print("  • Python")
    print("  • Git")
    print("  • Linux")
    print()
    print("==============================================")


def show_menu(name):

    print("\n")
    print("==============================================")
    print(f"          Welcome, {name}!")
    print("==============================================")
    print("1. Python Interview")
    print("2. Git Interview")
    print("3. Linux Interview")
    print("4. View My Progress")
    print("5. Exit")
    print("==============================================")


def select_difficulty(questions, topic, name):

    print("\n========== SELECT DIFFICULTY ==========")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Back")
    print("=======================================")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        difficulty = "Easy"

    elif choice == "2":
        difficulty = "Medium"

    elif choice == "3":
        difficulty = "Hard"

    elif choice == "4":
        return

    else:
        print("\nInvalid difficulty choice.")
        return

    selected_questions = [
        question
        for question in questions
        if question["difficulty"] == difficulty
    ]

    if not selected_questions:
        print("\nNo questions available.")
        return

    quiz = Quiz(
        selected_questions,
        f"{topic} - {difficulty}",
        name
    )

    quiz.start_quiz()


def get_user_results(name):

    try:

        with open("results.txt", "r") as file:
            results = file.readlines()

    except FileNotFoundError:

        return []

    user_results = []

    for result in results:

        if f"Candidate: {name}" in result:

            user_results.append(result.strip())

    return user_results


def show_progress(name):

    print("\n")
    print("==============================================")
    print("               MY PROGRESS")
    print("==============================================")

    user_results = get_user_results(name)

    if not user_results:

        print(f"\nNo results found for {name}.")
        print("Complete a quiz to start tracking progress!")
        print("==============================================")
        return

    print(f"\nCandidate: {name}")
    print()

    for number, result in enumerate(
        user_results,
        start=1
    ):

        parts = result.split(" | ")

        print(f"{number}. {parts[2]}")
        print(f"   {parts[3]}")
        print(f"   {parts[4]}")
        print()

    print("==============================================")


def show_performance_summary(name):

    print("\n")
    print("==============================================")
    print("          PERFORMANCE SUMMARY")
    print("==============================================")

    user_results = get_user_results(name)

    if not user_results:

        print("\nNo quiz attempts found.")
        print("Complete at least one quiz first.")
        print("==============================================")
        return

    percentages = []

    for result in user_results:

        parts = result.split(" | ")

        percentage_text = parts[4]

        percentage_text = (
            percentage_text
            .replace("Percentage: ", "")
            .replace("%", "")
        )

        try:

            percentage = float(percentage_text)
            percentages.append(percentage)

        except ValueError:

            continue

    if not percentages:

        print("\nUnable to calculate performance.")
        return

    total_quizzes = len(percentages)

    best_percentage = max(percentages)

    average_percentage = (
        sum(percentages) / total_quizzes
    )

    if average_percentage >= 80:

        rating = "Excellent 🏆"

    elif average_percentage >= 60:

        rating = "Good 👍"

    elif average_percentage >= 40:

        rating = "Needs Improvement 📚"

    else:

        rating = "Keep Practicing 💪"

    print()
    print(f"Candidate       : {name}")
    print(f"Quizzes Taken   : {total_quizzes}")
    print(f"Best Percentage : {best_percentage:.2f}%")
    print(f"Average Score   : {average_percentage:.2f}%")
    print()
    print(f"Overall Rating  : {rating}")

    print("==============================================")


def main():

    welcome()

    name = input("\nEnter your name: ").strip()

    if not name:

        name = "Candidate"

    print(f"\nWelcome, {name}! 👋")

    while True:

        show_menu(name)

        choice = input("\nEnter your choice: ")

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

            show_progress(name)

            print()

            show_performance_summary(name)

            input(
                "\nPress Enter to return to "
                "the main menu..."
            )

        elif choice == "5":

            print("\n==============================================")
            print(f"      Thank you, {name}!")
            print("      Keep learning and keep practicing! 🚀")
            print("==============================================")

            break

        else:

            print("\nInvalid choice.")
            print("Please select 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()