from commands import handle_task_command


def test_add_task_command():
    result = handle_task_command("add task Learn Python")

    assert result is not None


def test_add_interview_task_command():
    result = handle_task_command("add task Prepare for interview questions")

    assert result is not None


def test_show_task_command():
    result = handle_task_command("show task")

    assert result is not None