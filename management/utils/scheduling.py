import asyncio
import logging
from aiogram import Bot

from config.settings import AUTHORIZED_GROUPS
from ..commands import get_flower_url, get_landscape_url
from .handle_error import exception_handler


@exception_handler
async def send_photo_to_groups(
    bot: Bot, function: callable = get_flower_url, caption: str = "🌺🌺🌺"
):
    if not AUTHORIZED_GROUPS:
        return

    image_url, status = await function()
    if image_url is None:
        return

    for group_id in AUTHORIZED_GROUPS:
        await bot.send_photo(
            chat_id=group_id,
            photo=image_url,
            caption=caption,
        )


@exception_handler
async def scheduled(wait_for, bot: Bot):
    while True:
        await asyncio.sleep(wait_for)
        await send_photo_to_groups(bot)
        await send_photo_to_groups(bot, get_landscape_url, "🏕⛰🏔")
