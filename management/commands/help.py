from aiogram import Router, types
from aiogram.filters import Command
from config import settings

router = Router()


@router.message(Command("help"))
async def help_command(message: types.Message):
    help_string = f"""
    Я отправляю картинки в рандомные тайминги, с {settings.RANDOM_INTERVAL["min"]} до {settings.RANDOM_INTERVAL["max"]}.
    У меня не очень много токенов, но со временем их станет больше.
    По моим командам:
    /start - начало работы, в случае, если я в группе, то я инициализирую ее и смогу регулярно радовать вас контентом.
    /help - выводит это сообщение.
    /statistic - выводит статистику работы бота.
    /flower - отправляет цветок.
    /license - выводит информацию о моей лицензии.
    /get_flower - отправляет картинку цветка из открытой базы цветов.
    /get_landscape - отправляет картинку пейзажа из открытой базы пейзажей.
    """
    await message.answer(help_string)
