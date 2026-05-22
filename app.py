import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))


import streamlit as st

from src.preprocess import load_quiz_data, load_performance_data
from src.question_generator import generate_question, generate_ai_style_question
from src.difficulty_model import predict_difficulty
from src.recommendation_engine import calculate_topic_performance, recommend_topics
from src.performance_analytics import get_student_summary, get_topic_wise_analytics
from src.explanation_generator import generate_explanation, generate_topic_explanation


st.set_page_config(
    page_title="QuizSphere AI",
    page_icon="🧠",
    layout="wide"
)

st.title("QuizSphere AI – Adaptive Learning Platform")
st.subheader("AI-powered quiz generation, difficulty prediction, recommendations, analytics, and explanations")


quiz_df = load_quiz_data()
performance_df = load_performance_data()


st.divider()

st.header("Quiz Dataset")
st.dataframe(quiz_df, use_container_width=True)


st.divider()

st.header("Student Performance Data")
st.dataframe(performance_df, use_container_width=True)


st.divider()

st.header("AI Question Generator")

topic = st.selectbox(
    "Select Topic",
    ["Python", "Machine Learning", "Data Science", "SQL", "Backend", "DevOps", "Cloud"]
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Generate AI-Style Question"):
        generated = generate_ai_style_question(topic, difficulty)
        st.success(generated["generated_question"])
        st.write(f"Topic: {generated['topic']}")
        st.write(f"Difficulty: {generated['difficulty']}")

with col2:
    if st.button("Get Dataset Question"):
        dataset_question = generate_question(topic)

        if "error" in dataset_question:
            st.error(dataset_question["error"])
        else:
            st.success(dataset_question["question"])
            st.write(f"Correct Answer: {dataset_question['correct_answer']}")
            st.write(f"Difficulty: {dataset_question['difficulty']}")


st.divider()

st.header("AI Difficulty Prediction")

question_input = st.text_area(
    "Enter a quiz question",
    placeholder="Example: How would you optimize a machine learning model for production?"
)

if st.button("Predict Difficulty"):
    if question_input:
        predicted = predict_difficulty(question_input)
        st.info(f"Predicted Difficulty: {predicted}")
    else:
        st.warning("Please enter a question.")


st.divider()

st.header("Personalized Learning Recommendations")

student_id = st.number_input(
    "Enter Student ID",
    min_value=1,
    step=1
)

if st.button("Get Recommendations"):
    recommendations = recommend_topics(student_id)

    if isinstance(recommendations, dict) and "error" in recommendations:
        st.error(recommendations["error"])
    else:
        for rec in recommendations:
            if "message" in rec:
                st.success(rec["message"])
            else:
                st.write(f"Topic: {rec['topic']}")
                st.write(f"Accuracy: {rec['accuracy']}%")
                st.warning(rec["recommendation"])


st.divider()

st.header("Student Performance Analytics")

if st.button("Show Student Analytics"):
    summary = get_student_summary(student_id)
    topic_analytics = get_topic_wise_analytics(student_id)
    topic_performance = calculate_topic_performance(student_id)

    if isinstance(summary, dict) and "error" in summary:
        st.error(summary["error"])
    else:
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Questions", summary["total_questions"])
        col2.metric("Correct Answers", summary["correct_answers"])
        col3.metric("Accuracy", f"{summary['accuracy']}%")
        col4.metric("Avg Time", f"{summary['average_time_seconds']} sec")

        st.subheader("Topic-Wise Analytics")
        st.dataframe(topic_analytics, use_container_width=True)

        st.subheader("Topic Performance Summary")
        st.dataframe(topic_performance, use_container_width=True)

        chart_data = topic_analytics.set_index("topic")["accuracy"]
        st.bar_chart(chart_data)


st.divider()

st.header("LLM-Style Explanation Generator")

question = st.text_input("Question", "What is supervised learning?")
correct_answer = st.text_input("Correct Answer", "Learning from labeled data")
student_answer = st.text_input("Student Answer", "Learning by itself")

if st.button("Generate Explanation"):
    result = generate_explanation(question, correct_answer, student_answer)

    if result["result"] == "Correct":
        st.success(result["explanation"])
    else:
        st.error(result["result"])
        st.write(result["explanation"])


st.divider()

st.header("Topic Explanation")

selected_topic = st.selectbox(
    "Choose Topic for Explanation",
    ["Python", "Machine Learning", "Data Science", "SQL", "Backend", "DevOps", "Cloud"],
    key="topic_explanation"
)

if st.button("Explain Topic"):
    explanation = generate_topic_explanation(selected_topic)
    st.info(explanation)