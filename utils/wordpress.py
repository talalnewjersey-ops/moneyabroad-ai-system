import requests
import os

WP_URL = "https://moneyabroadguide.com/wp-json/wp/v2/posts"

WP_USER = os.getenv("WP_USER")
WP_PASSWORD = os.getenv("WP_PASSWORD")


def publish_post(title, content):

    data = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    response = requests.post(
        WP_URL,
        json=data,
        auth=(WP_USER, WP_PASSWORD)
    )

    print("WordPress response:", response.status_code)

    return response.json()