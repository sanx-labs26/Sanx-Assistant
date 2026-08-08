from command_parser import parse_task_command


def test_parse_task_command():
    result = parse_task_command(
        "Remind me to study Python tomorrow at 7 PM"
    )

    assert result is not None