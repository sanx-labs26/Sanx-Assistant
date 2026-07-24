import random

python_questions = [
    {
        "question": "What keyword is used to define a function in Python?",
        "answer": "def"
    },
    {
        "question": "Which data type is immutable?\nA) List\nB) Dictionary\nC) Tuple",
        "answer": "tuple"
    },
    {
        "question": "What loop is used to iterate over a sequence?",
        "answer": "for"
    }
]

sql_questions = [
    {
        "question": "Which SQL command retrieves data?",
        "answer": "select"
    },
    {
        "question": "Which clause filters rows?",
        "answer": "where"
    },
    {
        "question": "Which JOIN returns matching rows from both tables?",
        "answer": "inner join"
    }
]


def get_quiz(subject):
    subject = subject.lower()

    if "python" in subject:
        return random.choice(python_questions)

    elif "sql" in subject:
        return random.choice(sql_questions)

    else:
        return {
            "question": "Quiz not available for this subject.",
            "answer": ""
        }