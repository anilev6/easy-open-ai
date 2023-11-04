from ..models.picture import PictureGenerator, pic_saver
from typing import List


def get_picture_url(text: str) -> str:
    p = PictureGenerator(text)
    result = p.task()
    return result[0]


async def aget_picture_url(text: str) -> str:
    p = PictureGenerator(text)
    result = await p.async_task()
    return result[0]


def get_n_pictures_urls(text: str, n: int = 3) -> List[str]:
    """up to 10 pics"""
    p = PictureGenerator(text, n=n)
    result = p.task()
    return result


async def aget_n_pictures_urls(text: str, n: int = 3) -> List[str]:
    """up to 10 pics"""
    p = PictureGenerator(text, n=n)
    result = await p.async_task()
    return result


def get_picture(text: str, save: bool = True) -> str:
    p = PictureGenerator(text, format="b64_json")
    result = p.task()[0]
    if save:
        pic_saver(result, text)
    return result


async def aget_picture(text: str, save: bool = True) -> str:
    p = PictureGenerator(text, format="b64_json")
    result = await p.async_task()
    if save:
        pic_saver(result[0], text)
    return result


def get_n_pictures(text: str, n: int = 3, save: bool = True) -> List[str]:
    """up to 10 pics"""
    p = PictureGenerator(text, n=n, format="b64_json")
    result = p.task()
    if save:
        for i in range(len(result)):
            pic_saver(result[i], text + f"{i+1}")
    return result


async def aget_n_pictures(text: str, n: int = 3, save: bool = True) -> List[str]:
    """up to 10 pics"""
    p = PictureGenerator(text, n=n, format="b64_json")
    result = await p.async_task()
    if save:
        for i in range(len(result)):
            pic_saver(result[i], text[:15].replace(" ", "_") + f"{i+1}")
    return result
