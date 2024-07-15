import logging


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error: {func.__name__}: {e}")
            return None

    return wrapper
