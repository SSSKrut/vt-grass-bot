from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("У меня пока нет команд. Но скоро они появятся!")
