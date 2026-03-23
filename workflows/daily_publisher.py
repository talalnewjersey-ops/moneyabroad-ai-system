from agents.content_agent import create_article
from agents.seo_agent import optimize_seo
from utils.wordpress import publish_post

print("🚀 AI SYSTEM START")

articles = [
    {"kw": "best bank account for immigrants USA 2026", "country": "USA"},
    {"kw": "best bank account for newcomers Canada 2026", "country": "Canada"}
]

for item in articles:

    print("Generating:", item["kw"])

    article = create_article(item["kw"], item["country"])
    article = optimize_seo(article)

    publish_post(item["kw"], article)

    print("✅ Published:", item["kw"])