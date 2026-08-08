from placement import interview_mode


def test_hr_interview():
    result = interview_mode("hr")

    assert result is not None


def test_python_interview():
    result = interview_mode("python")

    assert result is not None


def test_sql_interview():
    result = interview_mode("sql")

    assert result is not None


def test_machine_learning_interview():
    result = interview_mode("machine learning")

    assert result is not None