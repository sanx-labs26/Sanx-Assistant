from quiz import get_quiz


def test_python_quiz():
    quiz = get_quiz("Python")

    assert quiz is not None
    assert isinstance(quiz, dict)
    assert "question" in quiz
    assert "answer" in quiz