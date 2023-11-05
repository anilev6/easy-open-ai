from ..models.stream_text import BaseChatCompletionStream, TranslateText, GetAnswerRhymes, GetPoem

def get_answer_with_instruction_stream(
    question: str,
    instruction: str,
    model="gpt-3.5-turbo",
    chaos_coefficient=0.5,
    max_tokens=1024,
) -> str:
    """The endpoint is ChatCompletion."""
    b = BaseChatCompletionStream(question, task_for_ai=instruction)
    b.model = model
    b.temperature = chaos_coefficient
    b.max_tokens = max_tokens
    for i in b.chat_completion_task():
        yield i


async def aget_answer_with_instruction_stream(
    question: str,
    instruction: str,
    model="gpt-3.5-turbo",
    chaos_coefficient=0.5,
    max_tokens=1024,
) -> str:
    """The endpoint is ChatCompletion."""
    b = BaseChatCompletionStream(question, task_for_ai=instruction)
    b.model = model
    b.temperature = chaos_coefficient
    b.max_tokens = max_tokens
    async for i in b.async_chat_completion_task():
        yield i

def get_answer_stream(question: str) -> str:
    b = BaseChatCompletionStream(question)
    b.temperature = 0.5
    for i in b.chat_completion_task():
        yield i


async def aget_answer_stream(question: str) -> str:
    b = BaseChatCompletionStream(question)
    b.temperature = 0.5
    async for i in b.async_chat_completion_task():
        yield i

def translate_text_stream(text: str, language="Ukrainian") -> str:
    t = TranslateText(text, target_language=language)
    for i in t.chat_completion_task():
        yield i


async def atranslate_text_stream(text: str, language="Ukrainian") -> str:
    t = TranslateText(text, target_language=language)
    async for i in t.async_chat_completion_task():
        yield i

def get_answer_as_poem_stream(question: str) -> str:
    b = GetAnswerRhymes(question)
    for i in b.chat_completion_task():
        yield i


async def aget_answer_as_poem_stream(question: str) -> str:
    b = GetAnswerRhymes(question)
    async for i in b.async_chat_completion_task():
        yield i


def get_poem_stream(text: str) -> str:
    b = GetPoem(text)
    for i in b.chat_completion_task():
        yield i


async def aget_poem_stream(text: str) -> str:
    b = GetPoem(text)
    async for i in b.async_chat_completion_task():
        yield i