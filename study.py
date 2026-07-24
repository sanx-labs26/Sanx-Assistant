def study_mode(topic):
    topic = topic.lower()

    if "python" in topic:
        return """
📘 Python

Python is a high-level, easy-to-learn programming language.

Key Topics:
• Variables
• Data Types
• Loops
• Functions
• OOP
• File Handling
• Exception Handling

Real-world uses:
• AI
• Data Science
• Web Development
• Automation

Interview Questions:
1. What is Python?
2. Difference between List and Tuple?
3. What is OOP?
"""

    elif "sql" in topic:
        return """
📘 SQL

SQL is used to manage databases.

Important Commands:
• SELECT
• INSERT
• UPDATE
• DELETE
• JOIN
• GROUP BY

Interview Questions:
1. What is a Primary Key?
2. Difference between WHERE and HAVING?
3. Explain INNER JOIN.
"""

    elif "machine learning" in topic:
        return """
📘 Machine Learning

Machine Learning allows computers to learn from data.

Types:
• Supervised Learning
• Unsupervised Learning
• Reinforcement Learning

Algorithms:
• Linear Regression
• Decision Tree
• Random Forest

Interview Questions:
1. What is Machine Learning?
2. What is Overfitting?
3. Difference between Classification and Regression?
"""

    else:
        return f"""
Sorry Sanx, I don't have notes for '{topic}' yet.
"""