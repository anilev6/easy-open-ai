import pytest
from icecream import ic
from easy_open_ai.functions.picture import (
    get_picture,
    get_n_pictures,
    get_picture_url,
    get_n_pictures_urls,
    aget_picture_url,
)
import asyncio


def test_get_picture():
    text = "a black kitty"
    ic(text)
    ic(get_picture(text))


def test_get_n_pictures():
    text = "a small kitty"
    ic(text)
    ic(get_n_pictures(text, n=2))


def test_get_picture_url():
    text = "a cute puppy"
    ic(text)
    ic(get_picture_url(text))


def test_get_n_pictures_urls():
    text = "a big puppy"
    ic(text)
    ic(get_n_pictures_urls(text))


# async def test_aget_picture_url():
#     text = "a cute puppy"
#     ic(text)
#     result = await aget_picture_url(text)
#     ic(result)


# async def test_errors_and_warnings():
#     l = [test_aget_picture_url() for _ in range(8)]
#     await asyncio.gather(*l)


if __name__ == "__main__":
    pytest.main([__file__, "-s"])

    # asyncio.run(test_errors_and_warnings())
