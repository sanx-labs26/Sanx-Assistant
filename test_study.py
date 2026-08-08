from study import study_mode


def test_python_study():
    result = study_mode("Python")

    assert result is not None


def test_sql_study():
    result = study_mode("SQL")

    assert result is not None


def test_machine_learning_study():
    result = study_mode("Machine Learning")

    assert result is not None