import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from preprocess import load_quiz_data, clean_quiz_data


MODEL_PATH = "models/difficulty_model.pkl"


def train_difficulty_model():
    quiz_df = clean_quiz_data(load_quiz_data())

    X = quiz_df["question"]
    y = quiz_df["difficulty"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Difficulty Model Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred, zero_division=0))

    joblib.dump(model, MODEL_PATH)
    print(f"Difficulty model saved to {MODEL_PATH}")


def predict_difficulty(question: str):
    model = joblib.load(MODEL_PATH)
    prediction = model.predict([question])
    return prediction[0]


if __name__ == "__main__":
    train_difficulty_model()

    test_question = "How would you optimize a machine learning model for production?"
    print("Predicted Difficulty:", predict_difficulty(test_question))