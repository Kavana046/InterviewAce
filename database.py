import sqlite3
from datetime import datetime


class InterviewDatabase:

    def __init__(self, database_name="interviewace.db"):

        self.database_name = database_name

        self.create_tables()

    # ==========================================
    # DATABASE CONNECTION
    # ==========================================

    def connect(self):

        return sqlite3.connect(
            self.database_name
        )

    # ==========================================
    # CREATE TABLES
    # ==========================================

    def create_tables(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate TEXT NOT NULL,
                topic TEXT NOT NULL,
                difficulty TEXT NOT NULL,
                score INTEGER NOT NULL,
                total_questions INTEGER NOT NULL,
                percentage REAL NOT NULL,
                grade TEXT NOT NULL,
                performance TEXT NOT NULL,
                date_time TEXT NOT NULL
            )
            """
        )

        connection.commit()

        connection.close()

    # ==========================================
    # SAVE RESULT
    # ==========================================

    def save_result(
        self,
        candidate,
        topic,
        difficulty,
        score,
        total_questions,
        percentage,
        grade,
        performance
    ):

        connection = self.connect()

        cursor = connection.cursor()

        date_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        cursor.execute(
            """
            INSERT INTO results (
                candidate,
                topic,
                difficulty,
                score,
                total_questions,
                percentage,
                grade,
                performance,
                date_time
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                candidate,
                topic,
                difficulty,
                score,
                total_questions,
                percentage,
                grade,
                performance,
                date_time
            )
        )

        connection.commit()

        connection.close()

    # ==========================================
    # GET ALL RESULTS
    # ==========================================

    def get_all_results(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                candidate,
                topic,
                difficulty,
                score,
                total_questions,
                percentage,
                grade,
                performance,
                date_time
            FROM results
            ORDER BY id DESC
            """
        )

        results = cursor.fetchall()

        connection.close()

        return results

    # ==========================================
    # GET LEADERBOARD
    # ==========================================

    def get_leaderboard(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                candidate,
                topic,
                difficulty,
                score,
                total_questions,
                percentage,
                grade
            FROM results
            ORDER BY percentage DESC
            LIMIT 10
            """
        )

        results = cursor.fetchall()

        connection.close()

        return results

    # ==========================================
    # GET TOTAL ATTEMPTS
    # ==========================================

    def get_total_attempts(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM results
            """
        )

        result = cursor.fetchone()

        connection.close()

        return result[0]

    # ==========================================
    # GET AVERAGE SCORE
    # ==========================================

    def get_average_percentage(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT AVG(percentage)
            FROM results
            """
        )

        result = cursor.fetchone()

        connection.close()

        if result[0] is None:

            return 0.0

        return result[0]

    # ==========================================
    # GET TOP SCORE
    # ==========================================

    def get_top_score(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT MAX(percentage)
            FROM results
            """
        )

        result = cursor.fetchone()

        connection.close()

        if result[0] is None:

            return 0.0

        return result[0]

    # ==========================================
    # CLEAR ALL RESULTS
    # ==========================================

    def clear_results(self):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM results
            """
        )

        connection.commit()

        connection.close()


# ==============================================
# TEST DATABASE
# ==============================================

if __name__ == "__main__":

    database = InterviewDatabase()

    print(
        "InterviewAce database created successfully."
    )

    print(
        f"Total attempts: "
        f"{database.get_total_attempts()}"
    )

    print(
        f"Average percentage: "
        f"{database.get_average_percentage():.2f}%"
    )

    print(
        f"Top score: "
        f"{database.get_top_score():.2f}%"
    )