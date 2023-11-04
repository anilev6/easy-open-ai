import pytest
from icecream import ic
import asyncio

from easy_open_ai.functions.text import (
    is_harmful_text,
    how_many_text_tokens,
    get_answer_with_instruction,
    translate_text,
    autocomplete_text,
    get_answer_as_poem,
    get_poem,
    sum_up_as_haiku,
    get_answer,
    correct_grammar,
    acorrect_grammar,
)

# ------------------------------------------------------Operations with text------------------------------------------------------------


def test_is_harmful_text():
    test_messages = ["I is doing well, fuck you fp asking."]
    for test_message in test_messages:
        ic(test_message)
        ic(is_harmful_text(test_message))


def test_how_many_text_tokens():
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
        ic(how_many_text_tokens(test_message))


def test_get_poem():
    test_text = "The internet is a global network of computers and other devices connected together, allowing people to share information and communicate with each other. It enables access to a wide range of resources such as websites, email, social media, online shopping, streaming services, and much more. The internet has revolutionized the way we connect, learn, work, and entertain ourselves."
    ic(test_text)
    ic(get_poem(test_text))


def test_translate_text():
    test_text = "I don't care"
    ic(test_text)
    ic(translate_text(test_text))


def test_autocomplete_text():
    test_text = "I don't care if you"
    ic(test_text)
    ic(autocomplete_text(test_text))


def test_get_answer_as_poem():
    test_question = "What is Python?"
    ic(test_question)
    ic(get_answer_as_poem(test_question))


def test_sum_up_as_haiku():
    test_text = "The internet is a global network of computers and other devices connected together, allowing people to share information and communicate with each other. It enables access to a wide range of resources such as websites, email, social media, online shopping, streaming services, and much more. The internet has revolutionized the way we connect, learn, work, and entertain ourselves."
    ic(test_text)
    ic(sum_up_as_haiku(test_text))


def test_get_answer():
    test_question = "what is internet?"
    ic(test_question)
    ic(get_answer(test_question))


def test_correct_grammar():
    test_text = "wht s internit?"
    ic(test_text)
    ic(correct_grammar(test_text))


def test_get_answer_with_instruction():
    test_question = "What is the meaning of life?"
    instruction = "You are a smart philosopher."
    ic(test_question, instruction)
    ic(get_answer_with_instruction(test_question, instruction))


# async def test_acorrect_grammar():
#     test_text='wht i thes'
#     ic(test_text)
#     result = await acorrect_grammar(test_text)
#     ic(result)

# async def test_errors_and_warnings():
#     l=[test_acorrect_grammar() for _ in range(8)]
#     await asyncio.gather(*l)

if __name__ == "__main__":
    pytest.main([__file__, "-s"])
    # asyncio.run(test_errors_and_warnings())
