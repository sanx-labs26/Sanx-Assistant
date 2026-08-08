from database import init_db
from reminder import print_reminders


def test_print_reminders():
    init_db()

    result = print_reminders()

    assert result is None or result is not False