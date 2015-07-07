from subprocess import Popen, PIPE


def process(input):
    p = Popen(['python3', './mailroom.py'],
              stdout=PIPE,
              stdin=PIPE,
              stderr=PIPE,
              )
    stdout, stderr = p.communicate(input=input)
    output = stdout.decode().lower()

    return output, stderr


def test_quit():
    output, error = process(b'quit')

    if "eoferror" in error.decode().lower():
        raise AssertionError("Quit unsuccessful")

    assert("send a (t)hank you" in output)
    assert("create a (r)eport" in output)


def test_thank_you_quit():
    output = process(b'T\n')[0]

    # prompts for a name
    assert("enter a name" in output)


def test_name_quit():
    output = process(b'T\nbill gates')[0]
    assert("donation amount" in output)


def test_name_donate():
    output, error = process(b'T\nbill gates\n200\nquit')

    if "eoferror" in error.decode().lower():
        raise AssertionError("Quit unsuccessful")

    # name and amount in thank you
    assert("bill gates" in output)
    assert("200" in output)

    # successfully returns to main menu
    assert("send a (t)hank you" in output)
    assert("create a (r)eport" in output)


def test_name_report():
    output, error = process(b'T\nbill gates\n200\nR\nquit')

    if "eoferror" in error.decode().lower():
        raise AssertionError("Quit unsuccessful")

    # new donor in report
    assert("bill gates" in output)
    assert("200" in output)
