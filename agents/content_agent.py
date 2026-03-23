from agents.utils.openai_client import generate_text

def create_article(keyword, country):

    prompt = f"""
You are a HIGH-LEVEL finance expert writing for MoneyAbroadGuide.com.

Create a PREMIUM, SEO-OPTIMIZED article.

TITLE:
"{keyword} in {country} (2026 Complete Guide)"

Audience: newcomers in {country}

Include:
- 3000+ words
- structured H1, H2, H3
- comparison table
- FAQ
- images placeholders
- internal links
- external links
- schema JSON
- CTA

Write in a human tone.
"""

    return generate_text(prompt)