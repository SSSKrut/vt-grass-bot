import logging
import random
from typing import Tuple
from aiogram import Router, types
from aiogram.filters import Command

from config import settings
from ..utils.search import unsplash

router = Router()


@router.message(Command("get_landscape"))
async def landscape_command(message: types.Message):
    count = random.randint(
        settings.LANDSCAPE_LIST_RANDOM["min"], settings.LANDSCAPE_LIST_RANDOM["max"]
    )
    count = min(count, len(settings.LANDSCAPE_LIST))
    query = random.sample(settings.LANDSCAPE_LIST, count)

    image_url, status = unsplash.random_image_unsplash(query)
    if image_url is None:
        await message.answer(f"Error: {status}")
        return

    await message.answer_photo(
        photo=image_url,
        caption="🏕⛰🏔",
    )


async def get_landscape_url() -> Tuple[str | None, int]:
    count = random.randint(
        settings.LANDSCAPE_LIST_RANDOM["min"], settings.LANDSCAPE_LIST_RANDOM["max"]
    )
    count = min(count, len(settings.LANDSCAPE_LIST))
    query = random.sample(settings.LANDSCAPE_LIST, count)

    image_url, status = unsplash.random_image_unsplash(query)
    if image_url is None:
        logging.error(f"Error: get landscape url: status {status}")
        return None, status

    return image_url, status
