"""Explanation generator utilities."""


def generate_explanation(question: str, correct_answer: str, student_answer: str):
    if student_answer.lower().strip() == correct_answer.lower().strip():
        return {
            "result": "Correct",
            "explanation": "Great job! Your answer matches the expected answer."
        }

    explanation = (
        f"The correct answer is: {correct_answer}. "
        f"Your answer was: {student_answer}. "
        f"To understand this better, focus on the main concept behind the question: '{question}'. "
        f"Review the topic and try solving a similar question again."
    )

    return {
        "result": "Incorrect",
        "explanation": explanation
    }


def generate_topic_explanation(topic: str):
    explanations = {
        "Python": "Python is a programming language used for software development, automation, AI, data science, and backend development.",
        "Machine Learning": "Machine Learning allows systems to learn patterns from data and make predictions without being explicitly programmed for every rule.",
        "Data Science": "Data Science focuses on collecting, cleaning, analyzing, and visualizing data to support decision-making.",
        "SQL": "SQL is used to store, query, update, and manage structured data in relational databases.",
        "Backend": "Backend development handles server-side logic, APIs, databases, authentication, and application workflows."
    }

    return explanations.get(
        topic,
        "This topic needs more review. Start with the basics, understand key terms, and practice examples."
    )


if __name__ == "__main__":
    question = "What is supervised learning?"
    correct_answer = "Learning from labeled data"
    student_answer = "Learning by itself"

    print(generate_explanation(question, correct_answer, student_answer))

    print("\nTopic Explanation:")
    print(generate_topic_explanation("Machine Learning"))