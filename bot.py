import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN, ADMIN_ID
from management.commands import start_router, help_router, flower_router, license_router

# from management.utils.handle_error import error_handler


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(start_router, help_router, flower_router, license_router)
    # dp.errors_handlers.register(error_handler)
    logging.info("Current admin list: %s", ADMIN_ID)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
