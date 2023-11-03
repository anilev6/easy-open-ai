from icecream import ic
import asyncio

# ------------------------------------------------------Operations with text------------------------------------------------------------

from easy_open_ai.models.text import IsHarmfulText, num_tokens_from_string


async def test_async_custom_task():
    # instructions_and_inputs = [("Reply me as a poet in rhymes", "How are you today?")]
    # for i in instructions_and_inputs:
    #     ic(i)
    pass


def try_all():
    all_sync_tests = (test_correct_grammar,)
    for t in all_sync_tests:
        t()


def test_correct_grammar():
    # test_messages = ["I is doing well, thnk you fp asking."]
    # for test_message in test_messages:
    #     ic(test_message)
    pass


def test_change_tone():
    pass


# need to add more tests!

# ------------------------------------------------------Validation------------------------------------------------------------


def test_is_harmful_text():
    test_messages = ["I is doing well, fuck you fp asking."]
    for test_message in test_messages:
        ic(test_message)
        ic(IsHarmfulText(test_message).validation_task())


def test_count_tokens():
    test_messages = [
        """Python, a language so profound,
        In the realm of coding, it is renowned.
        A versatile creature, graceful and sleek,
        With syntax elegant, simple and chic.

        A serpent of code, it slithers and slides,
        With power and speed, it gracefully glides.
        A language favored by many minds,
        For its readability and endless finds.

        Python, a friend to both novice and pro,
        With libraries galore, it helps us grow.
        From web development to data science's might,
        Python shines bright, guiding us through the night.

        Its community strong, supportive and vast,
        Python enthusiasts, united at last.
        From forums to meetups, they gather with glee,
        Sharing knowledge and code, setting spirits free."""
    ]
    for test_message in test_messages:
        ic(test_message)
        ic(num_tokens_from_string(test_message))


if __name__ == "__main__":
    # asyncio.run(test_async_custom_task())
    # test_correct_grammar()
    # test_is_harmful_text()
    test_count_tokens()
