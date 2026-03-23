from agents.content_agent import create_article
from utils.wordpress import publish_post

print("🚀 Starting AI publishing...")

articles = [
    {"kw": "best bank account for immigrants USA 2026", "country": "USA"},
    {"kw": "best bank account for newcomers Canada 2026", "country": "Canada"}
]

for item in articles:
    print(f"Generating: {item['kw']}")

    article = create_article(item["kw"], item["country"])

    publish_post(item["kw"], article)

    print(f"Draft created: {item['kw']}")
