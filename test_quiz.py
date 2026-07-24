from quiz import get_quiz

quiz = get_quiz("Python")

print("Question:")
print(quiz["question"])

print("\nAnswer:")
print(quiz["answer"])