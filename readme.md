# BudgetBeacon AI

AI-powered personal finance intelligence platform that tracks expenses, predicts spending, detects unusual transactions, and generates financial insights.

## Features

- Expense tracking dashboard
- AI transaction category prediction
- Monthly spending forecast
- Unusual transaction detection
- Financial insights generator
- Interactive Streamlit dashboard

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib

## Project Structure

```bash
budgetbeacon-ai/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── transactions.csv
├── src/
│   ├── preprocess.py
│   ├── train_category_model.py
│   ├── train_spending_model.py
│   ├── anomaly_detection.py
│   └── insights.py
├── models/
│   ├── category_model.pkl
│   ├── spending_model.pkl
│   └── anomaly_model.pkl
└── notebooks/
    └── eda.ipynb

#Installation
    git clone https://github.com/your-username/budgetbeacon-ai.git
cd budgetbeacon-ai
pip install -r requirements.txt

#Train Models
python src/train_category_model.py
python src/train_spending_model.py
python src/anomaly_detection.py

#Run App

streamlit run app.py

AI Modules
1. Category Prediction

Uses TF-IDF and Logistic Regression to classify transaction descriptions into expense categories.

2. Spending Forecast

Uses Linear Regression to predict next-month spending from historical monthly expense trends.

3. Anomaly Detection

Uses Isolation Forest to identify unusually high or abnormal expense transactions.

4. Financial Insights

Generates rule-based AI-style insights for savings, spending behavior, and category-level budgeting.
