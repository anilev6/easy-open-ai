"""operations with texts up to 1024 tokens (around 500 words)"""
from ..models.text import (
    BaseChatCompletion,
    GrammarCorrection,
    TranslateText,
    Autocomplete,
    GetPoem,
    GetAnswerRhymes,
    SummarizeHaiku,
    IsHarmfulText,
    num_tokens_from_string,
)


def is_harmful_text(text: str) -> list:
    """Free API call, unlimited. Returns list of the violations."""
    i = IsHarmfulText(text)
    result = i.validation_task()
    return result


# print(is_harmful_text("I h@te you"))


async def ais_harmful_text(text: str) -> list:
    """Free API call, unlimited. Returns list of the violations."""
    i = IsHarmfulText(text)
    result = await i.async_validation_task()
    return result


# import asyncio

# print(asyncio.run(ais_harmful_text("kel yourself")))


def how_many_text_tokens(text: str, model_name: str = "gpt-3.5-turbo") -> int:
    """Most of this package works with text no longer than 1024 tokens. This function makes no calls."""
    return num_tokens_from_string(text, model_name=model_name)


async def ahow_many_text_tokens(text: str, model_name: str = "gpt-3.5-turbo") -> int:
    """Most of this package works with text no longer than 1024 tokens. This function makes no calls."""
    return num_tokens_from_string(text, model_name=model_name)


# import asyncio

# print(asyncio.run(ahow_many_text_tokens("kel yourself")))


def get_answer_with_instruction(
    question: str,
    instruction: str,
    model="gpt-3.5-turbo",
    chaos_coefficient=0.5,
    max_tokens=1024,
) -> str:
    """The endpoint is ChatCompletion."""
    b = BaseChatCompletion(question, task_for_ai=instruction)
    b.model = model
    b.temperature = chaos_coefficient
    b.max_tokens = max_tokens
    result = b.chat_completion_task()
    return result


# print(
#     get_answer_with_instruction(
#         "You are my best friend I love you",
#         "your task is to return this text as a poem",
#     )
# )


async def aget_answer_with_instruction(
    question: str,
    instruction: str,
    model="gpt-3.5-turbo",
    chaos_coefficient=0.5,
    max_tokens=1024,
) -> str:
    """The endpoint is ChatCompletion."""
    b = BaseChatCompletion(question, task_for_ai=instruction)
    b.model = model
    b.temperature = chaos_coefficient
    b.max_tokens = max_tokens
    result = await b.async_chat_completion_task()
    return result


# import asyncio
# print(asyncio.run(aget_answer_with_instruction('You are my best friend I love you','your task is to return this text as a poem')))


def translate_text(text: str, language="Ukrainian") -> str:
    t = TranslateText(text, target_language=language)
    result = t.chat_completion_task()
    return result


# print(translate_text("I don't care"))


async def atranslate_text(text: str, language="Ukrainian") -> str:
    t = TranslateText(text, target_language=language)
    result = await t.async_chat_completion_task()
    return result


# import asyncio
# print(asyncio.run(atranslate_text("I don't care", language='Spanish')))


def autocomplete_text(text: str) -> str:
    b = Autocomplete(text)
    result = b.chat_completion_task()
    return result


# print(autocomplete_text("I don't care if you"))


async def aautocomplete_text(text: str) -> str:
    b = Autocomplete(text)
    result = await b.async_chat_completion_task()
    return result


# import asyncio
# print(asyncio.run(aautocomplete_text("Мені байдуже")))


def get_answer_as_poem(question: str) -> str:
    b = GetAnswerRhymes(question)
    result = b.chat_completion_task()
    return result


# print(get_answer_as_poem("What is Python?"))


async def aget_answer_as_poem(question: str) -> str:
    b = GetAnswerRhymes(question)
    result = await b.async_chat_completion_task()
    return result


# import asyncio
# print(asyncio.run(aget_answer_as_poem("Що таке Майкрософт?")))


def get_poem(text: str) -> str:
    b = GetPoem(text)
    result = b.chat_completion_task()
    return result


# print(get_poem("The internet is a global network of computers and other devices connected together, allowing people to share information and communicate with each other. It enables access to a wide range of resources such as websites, email, social media, online shopping, streaming services, and much more. The internet has revolutionized the way we connect, learn, work, and entertain ourselves."))


async def aget_poem(text: str) -> str:
    b = GetPoem(text)
    result = await b.async_chat_completion_task()
    return result


# import asyncio
# print(asyncio.run(aget_poem("The internet is a global network of computers and other devices connected together, allowing people to share information and communicate with each other. It enables access to a wide range of resources such as websites, email, social media, online shopping, streaming services, and much more. The internet has revolutionized the way we connect, learn, work, and entertain ourselves.")))


def sum_up_as_haiku(text: str) -> str:
    b = SummarizeHaiku(text)
    result = b.chat_completion_task()
    return result


# print(sum_up_as_haiku("The internet is a global network of computers and other devices connected together, allowing people to share information and communicate with each other. It enables access to a wide range of resources such as websites, email, social media, online shopping, streaming services, and much more. The internet has revolutionized the way we connect, learn, work, and entertain ourselves."))


async def asum_up_as_haiku(text: str) -> str:
    b = SummarizeHaiku(text)
    result = await b.async_chat_completion_task()
    return result


# import asyncio
# print(asyncio.run(asum_up_as_haiku("The internet is a global network of computers and other devices connected together, allowing people to share information and communicate with each other. It enables access to a wide range of resources such as websites, email, social media, online shopping, streaming services, and much more. The internet has revolutionized the way we connect, learn, work, and entertain ourselves.")))


def get_answer(question: str) -> str:
    task_for_ai = "You are a helpful assistant"
    b = BaseChatCompletion(question, task_for_ai=task_for_ai)
    b.temperature = 0.5
    result = b.chat_completion_task()
    return result


# print(get_answer('what is internet?'))


async def aget_answer(question: str) -> str:
    task_for_ai = "You are a helpful assistant"
    b = BaseChatCompletion(question, task_for_ai=task_for_ai)
    b.temperature = 0.5
    result = await b.async_chat_completion_task()
    return result


def correct_grammar(text: str) -> str:
    g = GrammarCorrection(text)
    result = g.chat_completion_task()
    return result


# print(correct_grammar('wht s internit?'))


async def acorrect_grammar(text: str) -> str:
    g = GrammarCorrection(text)
    result = await g.async_chat_completion_task()
    return result


# add more from text.py!
