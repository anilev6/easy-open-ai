from ..models.picture import PictureGenerator, pic_saver
from typing import List


def get_picture(text: str, save: bool = True) -> str:
    p = PictureGenerator(text, format="b64_json")
    result = p.task()[0]
    if save:
        pic_saver(result, text[:15].replace(" ", "_"))
    return result


# print(get_picture('a gorgeus cat'))


async def aget_picture(text: str, save: bool = True) -> str:
    p = PictureGenerator(text, format="b64_json")
    result = await p.async_task()
    if save:
        pic_saver(result[0], text[:15].replace(" ", "_"))
    return result


# import asyncio
# print(asyncio.run(aget_picture('girl power')))


def get_n_pictures(text: str, n: int = 3, save: bool = True) -> List[str]:
    """up to 10 pics"""
    p = PictureGenerator(text, n=n, format="b64_json")
    result = p.task()
    if save:
        for i in range(len(result)):
            pic_saver(result[i], text[:15].replace(" ", "_") + f"{i+1}")
    return result


# print(get_n_pictures('a gorgeus cat'))


async def aget_n_pictures(text: str, n: int = 3, save: bool = True) -> List[str]:
    """up to 10 pics"""
    p = PictureGenerator(text, n=n, format="b64_json")
    result = await p.async_task()
    if save:
        for i in range(len(result)):
            pic_saver(result[i], text[:15].replace(" ", "_") + f"{i+1}")
    return result


# import asyncio
# print(asyncio.run(aget_n_pictures('a flower')))

# add get pic urls
