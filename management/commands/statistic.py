import time
from aiogram import Router, types
from aiogram.filters import Command

from config import settings

router = Router()


@router.message(Command("statistic"))
async def statistic_command(message: types.Message):
    init_time = settings.BOT_INITIALIZED_TIME
    current_time = time.time()
    working_time = abs(current_time - init_time)

    days = int(working_time // (24 * 3600))
    working_time %= 24 * 3600
    hours = int(working_time // 3600)
    working_time %= 3600
    minutes = int(working_time // 60)
    seconds = int(working_time % 60)
    await message.answer(
        f"Бот работает без перезапусков {days} дней, {hours} часов, {minutes} минут и {seconds} секунд."
    )
