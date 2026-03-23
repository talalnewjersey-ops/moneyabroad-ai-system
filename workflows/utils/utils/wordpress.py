import requests
import os

def publish_post(title, content):
    url = "https://moneyabroadguide.com/wp-json/wp/v2/posts"

    response = requests.post(
        url,
        json={
            "title": title,
            "content": content,
            "status": "draft"
        },
        auth=(os.getenv("WP_USER"), os.getenv("WP_PASSWORD"))
    )

    return response.json()
