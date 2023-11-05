from ..models.stream_text import BaseChatCompletionStream


def stream_answer(question: str):
    """A generator."""
    for i in BaseChatCompletionStream(question).chat_completion_task():
        yield i


async def astream_answer(question: str):
    """A generator."""
    async for i in BaseChatCompletionStream(question).async_chat_completion_task():
        yield i
