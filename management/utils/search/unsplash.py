import requests
import logging
from typing import List, Tuple

import config
from .. import handle_error

url = "https://api.unsplash.com/photos/random"


@handle_error.exception_handler
def random_image_unsplash(query: List[str]) -> Tuple[bytes, int]:

    params = {
        "query": ", ".join(query),
        "client_id": config.UNSPLASH_TOKEN,
    }
    logging.info(f"Random_image_unsplash: params: {params}")
    response = requests.get(url, params=params)

    logging.info(
        f"Random_image_unsplash: response: status {response.status_code}, remaining {response.headers.get('X-Ratelimit-Remaining')}"
    )

    if response.status_code != 200:
        return None, response.status_code

    data = response.json()
    image_url = data["urls"]["regular"]
    logging.info(f"Image url: {image_url}")

    # image_response = requests.get(image_url)

    # if image_response.status_code != 200:
    #     logging.error(f"Random_image_unsplash: Error: {image_response.status_code}")
    #     return None, image_response.status_code

    return image_url, 200
