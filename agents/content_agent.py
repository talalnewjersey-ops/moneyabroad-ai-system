from agents.utils.openai_client import generate_text

def create_article(keyword, country):

    prompt = f"""
You are a finance expert writing for MoneyAbroadGuide.com.

Write a complete SEO article.

TITLE:
"{keyword} in {country} (2026 Guide)"

Audience:
Newcomers, immigrants, expats in {country}

Include:
- H1, H2, H3
- Comparison table
- FAQ
- Internal links
- CTA

Write in a human, clear tone.
"""

    return generate_text(prompt)