from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("flower"))
async def flower_command(message: types.Message):
    await message.answer("🌺")
