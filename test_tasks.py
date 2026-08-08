from database import init_db
from task_manager import (
    create_task,
    list_tasks,
    finish_task,
    remove_task,
)


def test_task_manager():
    init_db()

    # Create tasks
    create_result_1 = create_task(
        "Study Python",
        "Practice OOP",
        "2026-07-30",
    )

    create_result_2 = create_task(
        "Build SanX",
        "Complete Week 6",
        "2026-07-30",
    )

    assert create_result_1 is not None
    assert create_result_2 is not None

    # List tasks
    tasks = list_tasks()
    assert tasks is not None

    # Finish a task
    finish_result = finish_task(1)
    assert finish_result is not None

    # Remove a task
    remove_result = remove_task(2)
    assert remove_result is not None