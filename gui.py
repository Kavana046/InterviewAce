import tkinter as tk
from tkinter import messagebox, ttk
import random

from questions import (
    python_questions,
    git_questions,
    linux_questions
)

from performance import PerformanceAnalyzer
from database import InterviewDatabase


class InterviewAceGUI:

    def __init__(self, root):

        self.root = root

        self.root.title("InterviewAce")

        self.root.geometry("1000x700")

        self.root.resizable(False, False)

        self.bg_color = "#F4F7FB"
        self.primary_color = "#2563EB"
        self.secondary_color = "#1D4ED8"
        self.dark_color = "#111827"
        self.text_color = "#374151"
        self.gray_color = "#6B7280"
        self.card_color = "#FFFFFF"
        self.green_color = "#16A34A"
        self.red_color = "#DC2626"
        self.orange_color = "#EA580C"

        self.root.configure(
            bg=self.bg_color
        )

        self.database = InterviewDatabase()

        self.candidate_name = ""

        self.selected_topic = ""

        self.selected_questions = []

        self.current_questions = []

        self.current_question_index = 0

        self.current_difficulty = ""

        self.score = 0

        self.review_data = []

        self.analysis = {}

        self.answer_var = tk.StringVar()

        self.time_left = 10

        self.timer_id = None

        self.timer_label = None

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close_application
        )

        self.show_welcome_screen()

    # ==========================================
    # CLOSE APPLICATION
    # ==========================================

    def close_application(self):

        self.cancel_timer()

        self.root.destroy()

    # ==========================================
    # CANCEL TIMER
    # ==========================================

    def cancel_timer(self):

        if self.timer_id is not None:

            try:
                self.root.after_cancel(
                    self.timer_id
                )
            except Exception:
                pass

            self.timer_id = None

    # ==========================================
    # CLEAR SCREEN
    # ==========================================

    def clear_screen(self):

        self.cancel_timer()

        for widget in self.root.winfo_children():
            widget.destroy()

        self.timer_label = None

    # ==========================================
    # SAFE DATABASE OPERATION
    # ==========================================

    def database_error(self, error):

        messagebox.showerror(
            "Database Error",
            (
                "InterviewAce could not access "
                "the database.\n\n"
                f"Error:\n{error}"
            )
        )

    # ==========================================
    # BUTTON
    # ==========================================

    def create_button(
        self,
        parent,
        text,
        command,
        width=20
    ):

        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 11, "bold"),
            width=width,
            height=1,
            bg=self.primary_color,
            fg="white",
            activebackground=self.secondary_color,
            activeforeground="white",
            relief="flat",
            cursor="hand2"
        )

    # ==========================================
    # WELCOME SCREEN
    # ==========================================

    def show_welcome_screen(self):

        self.clear_screen()

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            frame,
            text="INTERVIEWACE",
            font=("Arial", 40, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            pady=(100, 5)
        )

        tk.Label(
            frame,
            text="Technical Interview Preparation Platform",
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(
            pady=5
        )

        tk.Label(
            frame,
            text="Practice • Improve • Succeed",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.gray_color
        ).pack(
            pady=5
        )

        tk.Label(
            frame,
            text="Enter your name",
            font=("Arial", 13, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(
            pady=(35, 8)
        )

        self.name_entry = tk.Entry(
            frame,
            font=("Arial", 15),
            width=30,
            justify="center"
        )

        self.name_entry.pack(
            ipady=8
        )

        self.create_button(
            frame,
            "START INTERVIEW",
            self.start_application,
            22
        ).pack(
            pady=25
        )

        tk.Label(
            frame,
            text="Python • Git • Linux",
            font=("Arial", 10),
            bg=self.bg_color,
            fg=self.gray_color
        ).pack(
            pady=10
        )

    # ==========================================
    # START APPLICATION
    # ==========================================

    def start_application(self):

        name = self.name_entry.get().strip()

        if not name:

            messagebox.showwarning(
                "Name Required",
                "Please enter your name before continuing."
            )

            self.name_entry.focus()

            return

        if len(name) < 2:

            messagebox.showwarning(
                "Invalid Name",
                "Please enter a valid name."
            )

            return

        self.candidate_name = name

        self.show_main_menu()

    # ==========================================
    # MAIN MENU
    # ==========================================

    def show_main_menu(self):

        self.clear_screen()

        header = tk.Frame(
            self.root,
            bg=self.primary_color,
            height=80
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="INTERVIEWACE",
            font=("Arial", 24, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack(
            side="left",
            padx=30
        )

        tk.Label(
            header,
            text=f"Welcome, {self.candidate_name}",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack(
            side="right",
            padx=30
        )

        content = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        content.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        tk.Label(
            content,
            text="Choose Your Interview",
            font=("Arial", 25, "bold"),
            bg=self.bg_color,
            fg=self.dark_color
        ).pack(
            pady=(0, 2)
        )

        tk.Label(
            content,
            text="Select a domain to begin your technical interview",
            font=("Arial", 11),
            bg=self.bg_color,
            fg=self.gray_color
        ).pack(
            pady=(0, 18)
        )

        cards = tk.Frame(
            content,
            bg=self.bg_color
        )

        cards.pack()

        self.create_topic_card(
            cards,
            "PYTHON",
            "Programming\n& Concepts",
            python_questions,
            0
        )

        self.create_topic_card(
            cards,
            "GIT",
            "Version Control\n& Commands",
            git_questions,
            1
        )

        self.create_topic_card(
            cards,
            "LINUX",
            "Operating System\n& Commands",
            linux_questions,
            2
        )

        tools = tk.Frame(
            content,
            bg=self.bg_color
        )

        tools.pack(
            pady=20
        )

        buttons = [
            ("Previous Results", self.show_results),
            ("Leaderboard", self.show_leaderboard),
            ("Statistics", self.show_statistics),
            ("Help", self.show_help),
            ("About", self.show_about),
            ("Clear Results", self.clear_results)
        ]

        for index, item in enumerate(buttons):

            self.create_button(
                tools,
                item[0],
                item[1],
                17
            ).grid(
                row=index // 3,
                column=index % 3,
                padx=5,
                pady=5
            )

        tk.Button(
            content,
            text="EXIT",
            command=self.close_application,
            font=("Arial", 10, "bold"),
            width=15,
            bg=self.gray_color,
            fg="white",
            relief="flat",
            cursor="hand2"
        ).pack(
            pady=2
        )

    # ==========================================
    # TOPIC CARD
    # ==========================================

    def create_topic_card(
        self,
        parent,
        title,
        description,
        questions,
        column
    ):

        card = tk.Frame(
            parent,
            bg=self.card_color,
            width=270,
            height=165,
            relief="solid",
            bd=1
        )

        card.grid(
            row=0,
            column=column,
            padx=8
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            font=("Arial", 20, "bold"),
            bg=self.card_color,
            fg=self.primary_color
        ).pack(
            pady=(15, 3)
        )

        tk.Label(
            card,
            text=description,
            font=("Arial", 10),
            bg=self.card_color,
            fg=self.gray_color,
            justify="center"
        ).pack(
            pady=3
        )

        tk.Label(
            card,
            text=f"{len(questions)} Questions",
            font=("Arial", 9, "bold"),
            bg=self.card_color,
            fg=self.text_color
        ).pack(
            pady=2
        )

        tk.Button(
            card,
            text="START",
            command=lambda: self.select_topic(
                title.title(),
                questions
            ),
            font=("Arial", 10, "bold"),
            bg=self.primary_color,
            fg="white",
            relief="flat",
            width=14,
            cursor="hand2"
        ).pack(
            pady=7
        )

    # ==========================================
    # SELECT TOPIC
    # ==========================================

    def select_topic(
        self,
        topic,
        questions
    ):

        if not questions:

            messagebox.showerror(
                "Question Error",
                f"No questions are available for {topic}."
            )

            return

        self.selected_topic = topic

        self.selected_questions = questions

        self.show_difficulty_screen()

    # ==========================================
    # DIFFICULTY
    # ==========================================

    def show_difficulty_screen(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text=self.selected_topic,
            font=("Arial", 30, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            pady=(65, 5)
        )

        tk.Label(
            self.root,
            text="Select Difficulty Level",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(
            pady=10
        )

        difficulties = [
            ("Easy", self.green_color),
            ("Medium", self.orange_color),
            ("Hard", self.red_color)
        ]

        for difficulty, color in difficulties:

            tk.Button(
                self.root,
                text=difficulty,
                command=lambda d=difficulty:
                self.start_quiz(d),
                font=("Arial", 12, "bold"),
                width=25,
                bg=color,
                fg="white",
                relief="flat",
                cursor="hand2"
            ).pack(
                pady=6
            )

        tk.Button(
            self.root,
            text="BACK",
            command=self.show_main_menu,
            font=("Arial", 10, "bold"),
            width=18,
            bg=self.gray_color,
            fg="white",
            relief="flat",
            cursor="hand2"
        ).pack(
            pady=25
        )

    # ==========================================
    # START QUIZ
    # ==========================================

    def start_quiz(self, difficulty):

        try:

            questions = [
                q
                for q in self.selected_questions
                if q.get("difficulty") == difficulty
            ]

        except Exception as error:

            messagebox.showerror(
                "Question Error",
                f"Unable to load questions.\n\n{error}"
            )

            return

        if not questions:

            messagebox.showwarning(
                "No Questions",
                f"No {difficulty} questions are available."
            )

            return

        self.current_difficulty = difficulty

        self.current_questions = questions.copy()

        random.shuffle(
            self.current_questions
        )

        self.current_question_index = 0

        self.score = 0

        self.review_data = []

        self.show_question()

    # ==========================================
    # SHOW QUESTION
    # ==========================================

    def show_question(self):

        self.clear_screen()

        if (
            self.current_question_index
            >= len(self.current_questions)
        ):

            self.show_final_result()

            return

        question = self.current_questions[
            self.current_question_index
        ]

        total = len(
            self.current_questions
        )

        number = self.current_question_index + 1

        header = tk.Frame(
            self.root,
            bg=self.primary_color,
            height=65
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text=f"{self.selected_topic} Interview",
            font=("Arial", 18, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack(
            side="left",
            padx=25
        )

        tk.Label(
            header,
            text=f"Score: {self.score}",
            font=("Arial", 12, "bold"),
            bg=self.primary_color,
            fg="white"
        ).pack(
            side="right",
            padx=25
        )

        info = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        info.pack(
            fill="x",
            padx=45,
            pady=(12, 3)
        )

        tk.Label(
            info,
            text=f"Question {number} of {total}",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(
            side="left"
        )

        tk.Label(
            info,
            text=self.current_difficulty,
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            side="right"
        )

        progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=900,
            mode="determinate"
        )

        progress["value"] = (
            number / total * 100
        )

        progress.pack(
            padx=45,
            pady=3
        )

        self.timer_label = tk.Label(
            self.root,
            text="Time: 10 seconds",
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg=self.orange_color
        )

        self.timer_label.pack(
            pady=5
        )

        question_frame = tk.Frame(
            self.root,
            bg=self.card_color,
            width=870,
            height=385,
            relief="solid",
            bd=1
        )

        question_frame.pack(
            pady=5
        )

        question_frame.pack_propagate(False)

        question_text = question.get(
            "question",
            ""
        )

        tk.Label(
            question_frame,
            text=question_text,
            font=("Arial", 15, "bold"),
            bg=self.card_color,
            fg=self.text_color,
            wraplength=780,
            justify="center"
        ).pack(
            pady=18
        )

        self.answer_var = tk.StringVar()

        options_frame = tk.Frame(
            question_frame,
            bg=self.card_color
        )

        options_frame.pack(
            fill="x",
            padx=50
        )

        options = question.get(
            "options",
            []
        )

        if not options:

            messagebox.showerror(
                "Question Error",
                "This question has no answer options."
            )

            self.move_to_next_question()

            return

        for index, option in enumerate(options):

            letter = chr(65 + index)

            tk.Radiobutton(
                options_frame,
                text=f"{letter}. {option}",
                variable=self.answer_var,
                value=letter,
                font=("Arial", 11),
                bg=self.card_color,
                fg=self.text_color,
                activebackground=self.card_color,
                selectcolor="#DBEAFE",
                anchor="w"
            ).pack(
                fill="x",
                pady=4
            )

        self.create_button(
            self.root,
            "SUBMIT ANSWER",
            self.submit_answer,
            22
        ).pack(
            pady=7
        )

        self.time_left = 10

        self.start_timer()

    # ==========================================
    # TIMER
    # ==========================================

    def start_timer(self):

        self.cancel_timer()

        self.update_timer()

    def update_timer(self):

        if self.timer_label is None:
            return

        if self.time_left > 0:

            self.timer_label.config(
                text=f"Time: {self.time_left} seconds"
            )

            self.time_left -= 1

            self.timer_id = self.root.after(
                1000,
                self.update_timer
            )

        else:

            self.timer_id = None

            messagebox.showinfo(
                "Time Up",
                "Time is over. Moving to the next question."
            )

            self.record_timeout()

    # ==========================================
    # TIMEOUT
    # ==========================================

    def record_timeout(self):

        if (
            self.current_question_index
            >= len(self.current_questions)
        ):
            return

        question = self.current_questions[
            self.current_question_index
        ]

        self.review_data.append(
            {
                "question": question.get(
                    "question",
                    ""
                ),
                "your_answer": "Not Answered",
                "correct_answer": question.get(
                    "answer",
                    ""
                )
            }
        )

        self.move_to_next_question()

    # ==========================================
    # SUBMIT ANSWER
    # ==========================================

    def submit_answer(self):

        self.cancel_timer()

        selected_answer = self.answer_var.get()

        if not selected_answer:

            messagebox.showwarning(
                "Answer Required",
                "Please select an answer."
            )

            self.start_timer()

            return

        if (
            self.current_question_index
            >= len(self.current_questions)
        ):
            return

        question = self.current_questions[
            self.current_question_index
        ]

        correct_answer = str(
            question.get(
                "answer",
                ""
            )
        ).upper()

        selected_answer = str(
            selected_answer
        ).upper()

        self.review_data.append(
            {
                "question": question.get(
                    "question",
                    ""
                ),
                "your_answer": selected_answer,
                "correct_answer": correct_answer
            }
        )

        if selected_answer == correct_answer:

            self.score += 1

            messagebox.showinfo(
                "Correct",
                "✓ Correct answer!"
            )

        else:

            messagebox.showinfo(
                "Incorrect",
                f"✗ Correct answer: {correct_answer}"
            )

        self.move_to_next_question()

    # ==========================================
    # NEXT QUESTION
    # ==========================================

    def move_to_next_question(self):

        self.cancel_timer()

        self.current_question_index += 1

        if (
            self.current_question_index
            >= len(self.current_questions)
        ):

            self.show_final_result()

        else:

            self.show_question()

    # ==========================================
    # FINAL RESULT
    # ==========================================

    def show_final_result(self):

        self.clear_screen()

        total = len(
            self.current_questions
        )

        try:

            analyzer = PerformanceAnalyzer(
                self.score,
                total
            )

            self.analysis = analyzer.get_analysis()

        except Exception as error:

            messagebox.showerror(
                "Performance Error",
                (
                    "Unable to calculate performance.\n\n"
                    f"{error}"
                )
            )

            return

        try:

            self.database.save_result(
                candidate=self.candidate_name,
                topic=self.selected_topic,
                difficulty=self.current_difficulty,
                score=self.analysis["score"],
                total_questions=self.analysis["total"],
                percentage=self.analysis["percentage"],
                grade=self.analysis["grade"],
                performance=self.analysis["performance"]
            )

        except Exception as error:

            self.database_error(error)

        self.display_final_result()

    # ==========================================
    # DISPLAY FINAL RESULT
    # ==========================================

    def display_final_result(self):

        # Clear the Question Review screen before showing the result.
        self.clear_screen()

        percentage = self.analysis["percentage"]

        grade = self.analysis["grade"]

        performance = self.analysis["performance"]

        correct = self.analysis["correct"]

        wrong = self.analysis["wrong"]

        tk.Label(
            self.root,
            text="INTERVIEW COMPLETED 🎉",
            font=("Arial", 28, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            pady=(25, 5)
        )

        tk.Label(
            self.root,
            text=(
                f"{self.selected_topic} • "
                f"{self.current_difficulty}"
            ),
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.gray_color
        ).pack()

        result_frame = tk.Frame(
            self.root,
            bg=self.card_color,
            width=850,
            height=350,
            relief="solid",
            bd=1
        )

        result_frame.pack(
            pady=12
        )

        result_frame.pack_propagate(False)

        tk.Label(
            result_frame,
            text=f"{correct}/{self.analysis['total']}",
            font=("Arial", 36, "bold"),
            bg=self.card_color,
            fg=self.primary_color
        ).pack(
            pady=(18, 0)
        )

        tk.Label(
            result_frame,
            text="FINAL SCORE",
            font=("Arial", 10, "bold"),
            bg=self.card_color,
            fg=self.gray_color
        ).pack()

        stats = tk.Frame(
            result_frame,
            bg=self.card_color
        )

        stats.pack(
            pady=15
        )

        self.create_stat_box(
            stats,
            "CORRECT",
            str(correct),
            self.green_color,
            0
        )

        self.create_stat_box(
            stats,
            "WRONG",
            str(wrong),
            self.red_color,
            1
        )

        self.create_stat_box(
            stats,
            "ACCURACY",
            f"{percentage:.1f}%",
            self.primary_color,
            2
        )

        self.create_stat_box(
            stats,
            "GRADE",
            grade,
            self.orange_color,
            3
        )

        tk.Label(
            result_frame,
            text=f"Performance: {performance}",
            font=("Arial", 14, "bold"),
            bg=self.card_color,
            fg=self.text_color
        ).pack(
            pady=5
        )

        buttons = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        buttons.pack()

        self.create_button(
            buttons,
            "Question Review",
            self.show_question_review,
            18
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        self.create_button(
            buttons,
            "Retry",
            lambda: self.start_quiz(
                self.current_difficulty
            ),
            15
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        self.create_button(
            buttons,
            "Dashboard",
            self.show_main_menu,
            15
        ).grid(
            row=0,
            column=2,
            padx=5
        )

    # ==========================================
    # STAT BOX
    # ==========================================

    def create_stat_box(
        self,
        parent,
        title,
        value,
        color,
        column
    ):

        box = tk.Frame(
            parent,
            bg="#F8FAFC",
            width=145,
            height=70,
            relief="solid",
            bd=1
        )

        box.grid(
            row=0,
            column=column,
            padx=5
        )

        box.pack_propagate(False)

        tk.Label(
            box,
            text=value,
            font=("Arial", 17, "bold"),
            bg="#F8FAFC",
            fg=color
        ).pack(
            pady=(8, 0)
        )

        tk.Label(
            box,
            text=title,
            font=("Arial", 8, "bold"),
            bg="#F8FAFC",
            fg=self.gray_color
        ).pack()

    # ==========================================
    # QUESTION REVIEW
    # ==========================================

    def show_question_review(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="QUESTION REVIEW",
            font=("Arial", 27, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            pady=18
        )

        frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=25
        )

        scrollbar = tk.Scrollbar(
            frame
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        text_box = tk.Text(
            frame,
            width=105,
            height=25,
            font=("Arial", 10),
            bg="white",
            wrap="word",
            yscrollcommand=scrollbar.set
        )

        text_box.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=text_box.yview
        )

        for number, item in enumerate(
            self.review_data,
            start=1
        ):

            your_answer = item["your_answer"]

            correct_answer = item["correct_answer"]

            status = (
                "CORRECT"
                if str(your_answer).upper()
                ==
                str(correct_answer).upper()
                else "INCORRECT"
            )

            text_box.insert(
                tk.END,
                f"{number}. {item['question']}\n\n"
            )

            text_box.insert(
                tk.END,
                f"Your Answer    : {your_answer}\n"
            )

            text_box.insert(
                tk.END,
                f"Correct Answer : {correct_answer}\n"
            )

            text_box.insert(
                tk.END,
                f"Result         : {status}\n\n"
            )

            text_box.insert(
                tk.END,
                "-" * 85 + "\n\n"
            )

        text_box.config(
            state="disabled"
        )

        self.create_button(
            self.root,
            "BACK TO RESULT",
            self.display_final_result,
            20
        ).pack(
            pady=8
        )

    # ==========================================
    # PREVIOUS RESULTS
    # ==========================================

    def show_results(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="PREVIOUS RESULTS",
            font=("Arial", 27, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            pady=18
        )

        try:

            results = self.database.get_all_results()

        except Exception as error:

            self.database_error(error)

            self.create_button(
                self.root,
                "BACK",
                self.show_main_menu,
                20
            ).pack(
                pady=20
            )

            return

        if not results:

            tk.Label(
                self.root,
                text="No previous results available.",
                font=("Arial", 15),
                bg=self.bg_color,
                fg=self.gray_color
            ).pack(
                pady=70
            )

        else:

            frame = tk.Frame(
                self.root
            )

            frame.pack(
                fill="both",
                expand=True,
                padx=20
            )

            scrollbar = tk.Scrollbar(
                frame
            )

            scrollbar.pack(
                side="right",
                fill="y"
            )

            text_box = tk.Text(
                frame,
                width=115,
                height=25,
                font=("Courier New", 9),
                yscrollcommand=scrollbar.set
            )

            text_box.pack(
                side="left",
                fill="both",
                expand=True
            )

            scrollbar.config(
                command=text_box.yview
            )

            for result in results:

                (
                    result_id,
                    candidate,
                    topic,
                    difficulty,
                    score,
                    total,
                    percentage,
                    grade,
                    performance,
                    date_time
                ) = result

                text_box.insert(
                    tk.END,
                    f"ID          : {result_id}\n"
                    f"Candidate   : {candidate}\n"
                    f"Topic       : {topic}\n"
                    f"Difficulty  : {difficulty}\n"
                    f"Score       : {score}/{total}\n"
                    f"Percentage  : {percentage:.2f}%\n"
                    f"Grade       : {grade}\n"
                    f"Performance : {performance}\n"
                    f"Date        : {date_time}\n"
                    + "=" * 85
                    + "\n\n"
                )

            text_box.config(
                state="disabled"
            )

        self.create_button(
            self.root,
            "BACK TO DASHBOARD",
            self.show_main_menu,
            20
        ).pack(
            pady=8
        )

    # ==========================================
    # LEADERBOARD
    # ==========================================

    def show_leaderboard(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="LEADERBOARD",
            font=("Arial", 27, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            pady=20
        )

        try:

            results = self.database.get_leaderboard()

        except Exception as error:

            self.database_error(error)

            self.create_button(
                self.root,
                "BACK",
                self.show_main_menu,
                20
            ).pack(
                pady=20
            )

            return

        if not results:

            tk.Label(
                self.root,
                text="No scores available yet.",
                font=("Arial", 15),
                bg=self.bg_color,
                fg=self.gray_color
            ).pack(
                pady=70
            )

        else:

            text_box = tk.Text(
                self.root,
                width=100,
                height=22,
                font=("Courier New", 10),
                bg="white"
            )

            text_box.pack(
                pady=10
            )

            text_box.insert(
                tk.END,
                "RANK | CANDIDATE       | TOPIC"
                "        | SCORE | PERCENTAGE | GRADE\n"
            )

            text_box.insert(
                tk.END,
                "-" * 90 + "\n"
            )

            for position, result in enumerate(
                results,
                start=1
            ):

                (
                    candidate,
                    topic,
                    difficulty,
                    score,
                    total,
                    percentage,
                    grade
                ) = result

                text_box.insert(
                    tk.END,
                    f"{position:<4} | "
                    f"{candidate[:15]:<15} | "
                    f"{topic[:12]:<12} | "
                    f"{score}/{total:<5} | "
                    f"{percentage:>8.2f}% | "
                    f"{grade}\n"
                )

            text_box.config(
                state="disabled"
            )

        self.create_button(
            self.root,
            "BACK TO DASHBOARD",
            self.show_main_menu,
            20
        ).pack(
            pady=8
        )

    # ==========================================
    # STATISTICS
    # ==========================================

    def show_statistics(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="QUESTION BANK STATISTICS",
            font=("Arial", 25, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            pady=20
        )

        topics = [
            ("Python", python_questions),
            ("Git", git_questions),
            ("Linux", linux_questions)
        ]

        text_box = tk.Text(
            self.root,
            width=60,
            height=18,
            font=("Courier New", 12),
            bg="white"
        )

        text_box.pack(
            pady=10
        )

        total_questions = 0

        for topic, questions in topics:

            easy = sum(
                1
                for q in questions
                if q.get("difficulty") == "Easy"
            )

            medium = sum(
                1
                for q in questions
                if q.get("difficulty") == "Medium"
            )

            hard = sum(
                1
                for q in questions
                if q.get("difficulty") == "Hard"
            )

            total = (
                easy
                + medium
                + hard
            )

            total_questions += total

            text_box.insert(
                tk.END,
                f"{topic}\n"
                f"{'-' * 35}\n"
                f"Easy   : {easy}\n"
                f"Medium : {medium}\n"
                f"Hard   : {hard}\n"
                f"Total  : {total}\n\n"
            )

        text_box.insert(
            tk.END,
            "=" * 35
            + "\n"
            + f"TOTAL QUESTIONS: {total_questions}"
        )

        text_box.config(
            state="disabled"
        )

        self.create_button(
            self.root,
            "BACK TO DASHBOARD",
            self.show_main_menu,
            20
        ).pack(
            pady=8
        )

    # ==========================================
    # HELP
    # ==========================================

    def show_help(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="HELP / INSTRUCTIONS",
            font=("Arial", 26, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            pady=25
        )

        instructions = (
            "HOW TO USE INTERVIEWACE\n\n"
            "1. Enter your name.\n\n"
            "2. Select Python, Git or Linux.\n\n"
            "3. Select Easy, Medium or Hard.\n\n"
            "4. Answer each question within 10 seconds.\n\n"
            "5. Questions are displayed randomly.\n\n"
            "6. Your score is calculated automatically.\n\n"
            "7. Review your answers after the interview.\n\n"
            "8. Results are saved automatically in SQLite.\n\n"
            "9. Previous Results shows your past attempts.\n\n"
            "10. Leaderboard shows the highest scores."
        )

        tk.Label(
            self.root,
            text=instructions,
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color,
            justify="left"
        ).pack(
            pady=10
        )

        self.create_button(
            self.root,
            "BACK TO DASHBOARD",
            self.show_main_menu,
            20
        ).pack(
            pady=15
        )

    # ==========================================
    # ABOUT
    # ==========================================

    def show_about(self):

        self.clear_screen()

        tk.Label(
            self.root,
            text="ABOUT INTERVIEWACE",
            font=("Arial", 27, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(
            pady=25
        )

        about = (
            "INTERVIEWACE\n\n"
            "A Python-based technical interview "
            "preparation platform.\n\n"
            "Technical Domains\n"
            "• Python\n"
            "• Git\n"
            "• Linux\n\n"
            "Main Features\n"
            "• Difficulty levels\n"
            "• Randomized questions\n"
            "• Timed interviews\n"
            "• Automatic scoring\n"
            "• Performance analysis\n"
            "• Grade calculation\n"
            "• Question review\n"
            "• SQLite database\n"
            "• Previous results\n"
            "• Leaderboard\n"
            "• Question statistics\n\n"
            "Technologies\n"
            "• Python\n"
            "• Tkinter\n"
            "• SQLite\n"
            "• Object-Oriented Programming\n"
            "• Git & GitHub"
        )

        tk.Label(
            self.root,
            text=about,
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color,
            justify="left"
        ).pack(
            pady=10
        )

        self.create_button(
            self.root,
            "BACK TO DASHBOARD",
            self.show_main_menu,
            20
        ).pack(
            pady=15
        )

    # ==========================================
    # CLEAR RESULTS
    # ==========================================

    def clear_results(self):

        answer = messagebox.askyesno(
            "Clear Results",
            (
                "Are you sure you want to delete "
                "ALL previous results?"
            )
        )

        if not answer:
            return

        try:

            self.database.clear_results()

            messagebox.showinfo(
                "Success",
                "All previous results have been deleted."
            )

        except Exception as error:

            self.database_error(error)


# ==============================================
# MAIN
# ==============================================

if __name__ == "__main__":

    root = tk.Tk()

    app = InterviewAceGUI(
        root
    )

    root.mainloop()
