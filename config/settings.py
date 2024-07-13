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
BOT_TOKEN = config["token"]

# Assign the 'admin' field as an array to ADMIN_ID
ADMIN_ID = config["admin"]
LICENSE = config["license"]
