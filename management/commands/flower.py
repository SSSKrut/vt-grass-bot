from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InputFile
from io import BytesIO

from ..utils.search import unsplash

router = Router()


@router.message(Command("flower"))
async def flower_command(message: types.Message):
    await message.answer("🌺")


@router.message(Command("get_flower"))
async def flower_command(message: types.Message):
    image_url, status = unsplash.random_image_unsplash(["flower"])

    if image_url is None:
        await message.answer(f"Error: {status}")
        return

    await message.answer_photo(
        photo=image_url,
        caption="🌺🌺🌺",
    )
