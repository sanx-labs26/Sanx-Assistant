import random

hr_questions = [
    "Tell me about yourself.",
    "Why should we hire you?",
    "What are your strengths?",
    "What are your weaknesses?",
    "Where do you see yourself in 5 years?",
    "Why do you want to join our company?",
    "Tell me about a challenge you faced and how you solved it.",
    "Why should we choose you over other candidates?"
]

python_questions = [
    "What is a Python list?",
    "Explain the difference between a List and a Tuple.",
    "What is a Dictionary in Python?",
    "Explain OOP in Python.",
    "What is Exception Handling?"
]

sql_questions = [
    "What is SQL?",
    "What is a Primary Key?",
    "Difference between WHERE and HAVING?",
    "Explain INNER JOIN.",
    "What is GROUP BY?"
]

ml_questions = [
    "What is Machine Learning?",
    "What is Supervised Learning?",
    "Difference between Classification and Regression?",
    "What is Overfitting?",
    "Explain Decision Tree."
]


def interview_mode(category):

    category = category.lower()

    if category == "hr":
        return random.choice(hr_questions)

    elif category == "python":
        return random.choice(python_questions)

    elif category == "sql":
        return random.choice(sql_questions)

    elif category == "machine learning":
        return random.choice(ml_questions)

    else:
        return "Sorry Sanx, interview questions are not available for this category."