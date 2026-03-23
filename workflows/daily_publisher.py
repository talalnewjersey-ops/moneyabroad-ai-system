import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from agents.content_agent import create_article
from agents.seo_agent import optimize_seo
from utils.wordpress import publish_post

print("🚀 AI SYSTEM START")

articles = [
    {"kw": "best bank account for immigrants USA"},
    {"kw": "best bank account for newcomers Canada"}
]

for item in articles:

    print("Generating:", item["kw"])

    article = create_article(item["kw"], "USA")
    article = optimize_seo(article)

    publish_post(item["kw"], article)

    print("✅ Published:", item["kw"])