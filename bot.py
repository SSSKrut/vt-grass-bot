import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import *
from management.utils import scheduled
from management.commands import (
    start_router,
    help_router,
    flower_router,
    license_router,
    landscape_router,
    statistic_router,
)


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        start_router,
        help_router,
        flower_router,
        license_router,
        landscape_router,
        statistic_router,
    )

    logging.info("Current admin list: %s", ADMIN_ID)
    logging.info("Current green list: %s", GREEN_LIST)
    logging.info("Current green random list: %s", GREEN_LIST_RANDOM)
    logging.info("Current landscape list: %s", GREEN_LIST)
    logging.info("Current landscape random list: %s", LANDSCAPE_LIST_RANDOM)
    logging.info("Current authorized groups: %s", AUTHORIZED_GROUPS)

    asyncio.create_task(scheduled(5, bot))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
