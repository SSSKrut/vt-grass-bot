import asyncio
from aiogram import Bot
from config.settings import AUTHORIZED_GROUPS


async def send_message_to_groups(bot: Bot):
    for group_id in AUTHORIZED_GROUPS:
        await bot.send_message(
            chat_id=group_id,
            text="I'm still alive",
        )


async def scheduled(wait_for, bot: Bot):
    while True:
        await asyncio.sleep(wait_for)
        await send_message_to_groups(bot)
