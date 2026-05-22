import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

QUIZ_DATA_PATH = BASE_DIR / "data" / "quiz_data.csv"
PERFORMANCE_DATA_PATH = BASE_DIR / "data" / "student_performance.csv"


def load_quiz_data():
    print("Loading quiz data from:")
    print(QUIZ_DATA_PATH)

    df = pd.read_csv(QUIZ_DATA_PATH)

    return df


def load_performance_data():
    print("Loading performance data from:")
    print(PERFORMANCE_DATA_PATH)

    df = pd.read_csv(PERFORMANCE_DATA_PATH)

    return df


def clean_quiz_data(df):
    df = df.copy()

    df = df.dropna()

    df["question"] = df["question"].astype(str)
    df["topic"] = df["topic"].astype(str)
    df["correct_answer"] = df["correct_answer"].astype(str)
    df["difficulty"] = df["difficulty"].astype(str)

    return df


def clean_performance_data(df):
    df = df.copy()

    df = df.dropna()

    df["student_id"] = df["student_id"].astype(int)
    df["student_name"] = df["student_name"].astype(str)
    df["topic"] = df["topic"].astype(str)
    df["question_id"] = df["question_id"].astype(int)
    df["is_correct"] = df["is_correct"].astype(int)
    df["time_taken_seconds"] = df["time_taken_seconds"].astype(int)

    return df


if __name__ == "__main__":
    quiz_df = load_quiz_data()
    performance_df = load_performance_data()

    print("\nQuiz Dataset")
    print(quiz_df.head())

    print("\nPerformance Dataset")
    print(performance_df.head())