import asyncio
from icecream import ic
from easy_open_ai.functions.stream_text import stream_answer, astream_answer


def test_stream_answer():
    result = ""
    for i in stream_answer("Tell me a fun geographical fact."):
        ic(i)
        result += i
    ic(result)


async def test_astream_answer():
    result = ""
    async for i in astream_answer("Tell me a fun geographical fact."):
        ic(i)
        result += i
    ic(result)


if __name__ == "__main__":
    test_stream_answer()
    asyncio.run(test_astream_answer())
