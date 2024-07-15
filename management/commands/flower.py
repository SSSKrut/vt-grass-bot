import logging
import random
from typing import Tuple
from aiogram import Router, types
from aiogram.filters import Command

from config import settings
from ..utils.search import unsplash

router = Router()


@router.message(Command("flower"))
async def flower_command(message: types.Message):
    await message.answer("🌺")


@router.message(Command("get_flower"))
async def flower_command(message: types.Message):
    count = random.randint(
        settings.GREEN_LIST_RANDOM["min"], settings.GREEN_LIST_RANDOM["max"]
    )
    count = min(count, len(settings.GREEN_LIST))
    query = random.sample(settings.GREEN_LIST, count)

    image_url, status = unsplash.random_image_unsplash(query)
    if image_url is None:
        await message.answer(f"Error: {status}")
        return

    await message.answer_photo(
        photo=image_url,
        caption="🌺🌺🌺",
    )


async def get_flower_url() -> Tuple[str | None, int]:
    count = random.randint(
        settings.GREEN_LIST_RANDOM["min"], settings.GREEN_LIST_RANDOM["max"]
    )
    count = min(count, len(settings.GREEN_LIST))
    query = random.sample(settings.GREEN_LIST, count)

    image_url, status = unsplash.random_image_unsplash(query)
    if image_url is None:
        logging.error(f"Error: get flower url: status {status}")
        return None, status

    return image_url, status
