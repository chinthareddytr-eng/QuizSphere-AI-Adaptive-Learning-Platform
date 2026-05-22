import random
from preprocess import load_quiz_data, clean_quiz_data


def generate_question(topic: str):
    quiz_df = clean_quiz_data(load_quiz_data())

    topic_questions = quiz_df[
        quiz_df["topic"].str.lower() == topic.lower()
    ]

    if topic_questions.empty:
        return {
            "error": f"No questions found for topic: {topic}"
        }

    selected = topic_questions.sample(1).iloc[0]

    return {
        "question": selected["question"],
        "topic": selected["topic"],
        "correct_answer": selected["correct_answer"],
        "difficulty": selected["difficulty"]
    }


def generate_ai_style_question(topic: str, difficulty: str):
    templates = {
        "Easy": [
            f"What is the basic meaning of {topic}?",
            f"Why is {topic} important for beginners?",
            f"Explain one simple concept in {topic}."
        ],
        "Medium": [
            f"How is {topic} applied in real-world projects?",
            f"What problem does {topic} solve?",
            f"Explain {topic} with an example."
        ],
        "Hard": [
            f"How would you design a system using {topic}?",
            f"What are the trade-offs involved in {topic}?",
            f"How can {topic} be optimized for production?"
        ]
    }

    question = random.choice(templates.get(difficulty, templates["Easy"]))

    return {
        "generated_question": question,
        "topic": topic,
        "difficulty": difficulty
    }


if __name__ == "__main__":
    print("Question From Dataset:")
    print(generate_question("Python"))

    print("\nAI-Style Generated Question:")
    print(generate_ai_style_question("Machine Learning", "Medium"))