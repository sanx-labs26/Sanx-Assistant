import subprocess


def test_notepad_can_start():
    process = subprocess.Popen("notepad.exe")

    assert process.poll() is None

    process.terminate()
