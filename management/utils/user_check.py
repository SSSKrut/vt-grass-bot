from aiogram import types
from config.settings import ADMIN_ID


async def get_user_from_message(message: types.Message):
    user = message.from_user
    return user
