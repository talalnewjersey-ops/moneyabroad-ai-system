import requests
import os

def publish_post(title, content):

    url = "https://moneyabroadguide.com/wp-json/wp/v2/posts"

    data = {
        "title": title,
        "content": content,
        "status": "draft"   # 🔥 IMPORTANT
    }

    response = requests.post(
        url,
        auth=(os.getenv("WP_USER"), os.getenv("WP_PASSWORD")),
        json=data
    )

    print("Draft created:", response.status_code)