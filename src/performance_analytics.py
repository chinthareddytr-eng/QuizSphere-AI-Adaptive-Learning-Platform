
from preprocess import load_performance_data, clean_performance_data


def get_student_summary(student_id: int):
    performance_df = clean_performance_data(load_performance_data())

    student_df = performance_df[
        performance_df["student_id"] == student_id
    ]

    if student_df.empty:
        return {
            "error": f"No data found for student_id: {student_id}"
        }

    total_questions = len(student_df)
    correct_answers = student_df["is_correct"].sum()
    accuracy = (correct_answers / total_questions) * 100
    average_time = student_df["time_taken_seconds"].mean()

    return {
        "student_id": student_id,
        "total_questions": total_questions,
        "correct_answers": int(correct_answers),
        "accuracy": round(accuracy, 2),
        "average_time_seconds": round(average_time, 2)
    }


def get_topic_wise_analytics(student_id: int):
    performance_df = clean_performance_data(load_performance_data())

    student_df = performance_df[
        performance_df["student_id"] == student_id
    ]

    if student_df.empty:
        return {
            "error": f"No data found for student_id: {student_id}"
        }

    topic_summary = (
        student_df
        .groupby("topic")
        .agg(
            total_questions=("is_correct", "count"),
            correct_answers=("is_correct", "sum"),
            average_time=("time_taken_seconds", "mean")
        )
        .reset_index()
    )

    topic_summary["accuracy"] = (
        topic_summary["correct_answers"] /
        topic_summary["total_questions"]
    ) * 100

    return topic_summary


if __name__ == "__main__":
    student_id = 1

    print("Student Summary:")
    print(get_student_summary(student_id))

    print("\nTopic Wise Analytics:")
    print(get_topic_wise_analytics(student_id))