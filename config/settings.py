import logging
import yaml

try:
    with open(".config.yaml", "r") as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            logging.error("Error reading the config file")
            print(exc)
except FileNotFoundError:
    logging.error("Config file not found")


# Read the token from the file
BOT_TOKEN = config["telegram_token"]
UNSPLASH_TOKEN = config["unsplash_token"]

GREEN_LIST = config["green_list"]
GREEN_LIST_RANDOM = config["green_list_random"]

LANDSCAPE_LIST = config["landscape_list"]
LANDSCAPE_LIST_RANDOM = config["landscape_list_random"]

# Assign the 'admin' field as an array to ADMIN_ID
ADMIN_ID = config["admin"]
LICENSE = config["license"]
