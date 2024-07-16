import asyncio
import random
import time
import logging
from typing import Tuple
from datetime import datetime, timedelta
from aiogram import Bot

from config import *
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
def is_interval_time() -> bool:
    # Check if the current time is within the random range time interval
    current_hour = time.localtime().tm_hour
    if RANDOM_INTERVAL["min"] < RANDOM_INTERVAL["max"]:
        return RANDOM_INTERVAL["min"] <= current_hour < RANDOM_INTERVAL["max"]
    else:
        return (
            current_hour >= RANDOM_INTERVAL["min"]
            or current_hour < RANDOM_INTERVAL["max"]
        )


@exception_handler
def random_func_photo_get(functions: list[callable], weight: list[int]) -> callable:
    return random.choices(functions, weight, k=1)[0]


@exception_handler
def get_random_post_time(count: int) -> list[int]:
    now = datetime.now()
    start_of_day = datetime(now.year, now.month, now.day)
    start_of_next_day = start_of_day + timedelta(days=1)

    start_of_day_unix = int(start_of_day.timestamp())
    start_of_next_day_unix = int(start_of_next_day.timestamp())
    now_unix = int(now.timestamp())

    start_of_posting_unix = start_of_day_unix + RANDOM_INTERVAL["min"] * 3600
    end_of_posting_unix = start_of_day_unix + RANDOM_INTERVAL["max"] * 3600

    # Checking if the config was changed
    start_of_posting_unix = max(start_of_posting_unix, now_unix)
    if start_of_posting_unix >= end_of_posting_unix:
        return []

    post_time_list = []
    for i in range(count):
        random_post_time = random.randint(start_of_posting_unix, end_of_posting_unix)
        post_time_list.append(random_post_time)

    post_time_list.sort()
    return post_time_list


@exception_handler
def how_much_wait_seconds(timestamp_unix: int) -> int:
    now = datetime.now()
    now_unix = int(now.timestamp())
    if timestamp_unix > now_unix:
        return timestamp_unix - now_unix
    else:
        return 0


@exception_handler
async def day_schedule(wait_for: int, bot: Bot):
    post_time = []
    photos_sended_today = 0
    today = datetime.now().day

    photos_to_send = RANDOM_INTERVAL["count"] - photos_sended_today
    if photos_to_send <= 0:
        return

    if not post_time:
        post_time = get_random_post_time(photos_to_send)

    logging.info(
        "Waiting to send photo(s) at "
        + ", ".join(
            [
                time.strftime("%H:%M:%S", time.localtime(timestamp))
                for timestamp in post_time
            ]
        )
    )

    while today == datetime.now().day:
        await asyncio.sleep(wait_for)

        if not is_interval_time():
            continue

        if not post_time:
            # All photos are sent already
            continue

        if datetime.now().timestamp() < post_time[0]:
            continue

        post_time.pop(0)
        func = random_func_photo_get([get_flower_url, get_landscape_url], [3, 1])

        if func == get_flower_url:
            await send_photo_to_groups(bot, func, "🌺🌺🌺")
        elif func == get_landscape_url:
            await send_photo_to_groups(bot, func, "🏕⛰🏔")
        else:
            await send_photo_to_groups(bot, func)
        photos_sended_today += 1


@exception_handler
async def scheduled(wait_for, bot: Bot):
    while True:
        await day_schedule(wait_for, bot)
