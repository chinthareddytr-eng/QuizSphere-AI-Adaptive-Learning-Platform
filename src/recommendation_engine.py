
from preprocess import load_performance_data, clean_performance_data


def calculate_topic_performance(student_id: int):
    performance_df = clean_performance_data(load_performance_data())

    student_df = performance_df[
        performance_df["student_id"] == student_id
    ]

    if student_df.empty:
        return {
            "error": f"No performance data found for student_id: {student_id}"
        }

    topic_performance = (
        student_df
        .groupby("topic")
        .agg(
            total_questions=("is_correct", "count"),
            correct_answers=("is_correct", "sum"),
            average_time=("time_taken_seconds", "mean")
        )
        .reset_index()
    )

    topic_performance["accuracy"] = (
        topic_performance["correct_answers"] /
        topic_performance["total_questions"]
    ) * 100

    return topic_performance


def recommend_topics(student_id: int):
    topic_performance = calculate_topic_performance(student_id)

    if isinstance(topic_performance, dict):
        return topic_performance

    weak_topics = topic_performance[
        topic_performance["accuracy"] < 70
    ]

    recommendations = []

    for _, row in weak_topics.iterrows():
        recommendations.append(
            {
                "topic": row["topic"],
                "accuracy": round(row["accuracy"], 2),
                "recommendation": f"Revise {row['topic']} because your accuracy is below 70%."
            }
        )

    if not recommendations:
        recommendations.append(
            {
                "message": "Great job! No weak topics found. Continue practicing advanced questions."
            }
        )

    return recommendations


if __name__ == "__main__":
    student_id = 1

    print("Topic Performance:")
    print(calculate_topic_performance(student_id))

    print("\nPersonalized Recommendations:")
    print(recommend_topics(student_id))