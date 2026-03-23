from utils.openai_client import generate_text

def create_article(keyword, country):
    prompt = f"""
Write a 3500-word SEO article for newcomers in {country}.

Keyword: {keyword}

Include:
- Table of contents
- 2 realistic stories
- comparison table
- FAQ
- disclaimer
"""

    return generate_text(prompt)
