import asyncio
import pytest
from icecream import ic

from easy_open_ai.functions.stream_text import (
    get_answer_stream,
    get_answer_as_poem_stream,
    get_answer_with_instruction_stream,
    get_poem_stream,
    aget_poem_stream,
    translate_text_stream,
)


def test_get_poem_stream():
    test_text = "The internet is a global network of computers and other devices connected together, allowing people to share information and communicate with each other. It enables access to a wide range of resources such as websites, email, social media, online shopping, streaming services, and much more. The internet has revolutionized the way we connect, learn, work, and entertain ourselves."
    ic(test_text)
    for i in get_poem_stream(test_text):
        ic(i)


def test_translate_text_stream():
    test_text = "I don't care"
    ic(test_text)
    for i in translate_text_stream(test_text):
        ic(i)


def test_get_answer_as_poem_stream():
    test_question = "What is Python?"
    ic(test_question)
    for i in get_answer_as_poem_stream(test_question):
        ic(i)


def test_get_answer_stream():
    test_question = "what is internet?"
    ic(test_question)
    for i in get_answer_stream(test_question):
        ic(i)


def test_get_answer_with_instruction_stream():
    test_question = "What is the meaning of life?"
    instruction = "You are a smart philosopher."
    ic(test_question, instruction)
    for i in get_answer_with_instruction_stream(test_question, instruction):
        ic(i)


# async def test_aget_poem_stream():
#     test_text = "The internet is a global network of computers and other devices connected together, allowing people to share information and communicate with each other. It enables access to a wide range of resources such as websites, email, social media, online shopping, streaming services, and much more. The internet has revolutionized the way we connect, learn, work, and entertain ourselves."
#     ic(test_text)
#     async for i in aget_poem_stream(test_text):
#         ic(i)


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
    # asyncio.run(test_aget_poem_stream())
