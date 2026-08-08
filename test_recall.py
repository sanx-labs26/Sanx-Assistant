from database import init_db, get_recent_conversations


def test_recall_conversations():
    init_db()

    history = get_recent_conversations()

    assert history is not None