from aiogram import Router, types
from aiogram.filters import Command

from config.settings import LICENSE

router = Router()


@router.message(Command("license"))
async def flower_command(message: types.Message):
    await message.answer(LICENSE)
    await message.answer("🌺")
