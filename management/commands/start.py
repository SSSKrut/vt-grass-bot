from aiogram import Router, types
from aiogram.filters import Command
from config import settings

router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    group = ["group", "supergroup"]
    if message.chat.type not in group:
        await message.answer(f"Привет! Я бот для отправки травы.")
        return

    settings.AUTHORIZED_GROUPS.add(message.chat.id)
    answer = (
        f"Привет! Я бот для отправки травы.\n"
        f"Группа {message.chat.title} инициализирована.\n"
        f"Я буду иногда отправлять сюда красивые картинки. "
        f"В /help есть немного полезной информации."
    )

    await message.answer(answer)


@router.message(Command("stop"))
async def stop_command(message: types.Message):
    group = ["group", "supergroup"]
    if message.chat.type not in group:
        await message.answer(f"Пока!.")
        return
    try:
        settings.AUTHORIZED_GROUPS.remove(message.chat.id)
    except KeyError:
        None
    answer = "Группа деактивирована. Пока!"

    await message.answer(answer)
