import logging


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error: {func.__name__}: {e}")
            return None

    return wrapper


# def async_conditional_exception_handler(condition_check):
#     def decorator(func):
#         async def wrapper(*args, **kwargs):
#             if not condition_check():
#                 return None
#             try:
#                 return await func(*args, **kwargs)
#             except Exception as e:
#                 logging.error(f"Error in {func.__name__}: {e}")
#                 return None

#         return wrapper

#     return decorator
