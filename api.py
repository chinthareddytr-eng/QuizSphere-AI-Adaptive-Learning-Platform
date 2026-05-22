from fastapi import FastAPI
from pydantic import BaseModel

from src.question_generator import generate_ai_style_question
from src.difficulty_model import predict_difficulty
from src.recommendation_engine import recommend_topics
from src.performance_analytics import get_student_summary, get_topic_wise_analytics
from src.explanation_generator import generate_explanation, generate_topic_explanation


app = FastAPI(title="QuizSphere AI API")


class QuestionRequest(BaseModel):
    topic: str
    difficulty: str


class DifficultyRequest(BaseModel):
    question: str


class ExplanationRequest(BaseModel):
    question: str
    correct_answer: str
    student_answer: str


@app.get("/")
def home():
    return {"message": "QuizSphere AI API is running"}


@app.post("/generate-question")
def generate_question(request: QuestionRequest):
    return generate_ai_style_question(
        request.topic,
        request.difficulty
    )


@app.post("/predict-difficulty")
def difficulty_prediction(request: DifficultyRequest):
    prediction = predict_difficulty(request.question)

    return {
        "question": request.question,
        "predicted_difficulty": prediction
    }


@app.get("/recommendations/{student_id}")
def get_recommendations(student_id: int):
    return {
        "student_id": student_id,
        "recommendations": recommend_topics(student_id)
    }


@app.get("/analytics/{student_id}")
def get_analytics(student_id: int):
    summary = get_student_summary(student_id)
    topic_analytics = get_topic_wise_analytics(student_id)

    if isinstance(topic_analytics, dict):
        topic_data = topic_analytics
    else:
        topic_data = topic_analytics.to_dict(orient="records")

    return {
        "summary": summary,
        "topic_analytics": topic_data
    }


@app.post("/generate-explanation")
def explanation(request: ExplanationRequest):
    return generate_explanation(
        request.question,
        request.correct_answer,
        request.student_answer
    )


@app.get("/topic-explanation/{topic}")
def topic_explanation(topic: str):
    return {
        "topic": topic,
        "explanation": generate_topic_explanation(topic)
    }
