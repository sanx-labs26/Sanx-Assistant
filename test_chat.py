from chat_engine import chat


def test_chat_returns_response():
    response = chat("Hello SanX")

    assert response is not None
    assert isinstance(response, str)
    assert response.strip() != ""