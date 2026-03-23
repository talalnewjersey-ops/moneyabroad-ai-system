from agents.utils.openai_client import generate_text

def optimize_seo(article):

    prompt = f"""
Improve this article for SEO (Google ranking):

- Add meta title (60 chars)
- Add meta description (160 chars)
- Improve readability
- Optimize headings
- Add keyword variations
- Add internal linking suggestions
- Improve E-E-A-T signals

Article:
{article}
"""

    return generate_text(prompt)