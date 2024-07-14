import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import *
from management.commands import start_router, help_router, flower_router, license_router
import management.utils
import management.utils.search

# from management.utils.handle_error import error_handler


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(start_router, help_router, flower_router, license_router)
    # dp.errors_handlers.register(error_handler)
    logging.info("Current admin list: %s", ADMIN_ID)
    logging.info("Current green list: %s", GREEN_LIST)
    logging.info("Current green random list: %s", GREEN_LIST_RANDOM)
    logging.info("Current landscape list: %s", GREEN_LIST)
    logging.info("Current landscape random list: %s", LANDSCAPE_LIST_RANDOM)

    # management.utils.search.random_image_unsplash(["flower"])

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
