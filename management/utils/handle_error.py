# import logging
# from aiogram.exceptions import BlockedByUser


# async def error_handler(update, exception):
#     if isinstance(exception, BlockedByUser):
#         logging.error(f"Bot was blocked by the user {update.message.chat.id}")
#     else:
#         logging.error(f"Unexpected error: {exception}")
#     return True
