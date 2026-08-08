from progress import (
    create_progress_table,
    save_progress,
    get_progress,
)


def test_progress_tracking():
    create_progress_table()

    save_progress("Python", "Completed", 9)
    save_progress("SQL", "Completed", 8)
    save_progress("Machine Learning", "Learning", 6)

    rows = get_progress()

    assert rows is not None
    assert len(rows) >= 3