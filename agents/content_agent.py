from utils.openai_client import generate_text

def create_article(keyword, country):

    prompt = f"""
    Write a detailed SEO article about: {keyword}

    Target: newcomers in {country}

    Requirements:
    - Minimum 1500 words (test version)
    - Include introduction
    - Include sections with headings
    - Include conclusion
    - Make it helpful and practical
    """

    article = generate_text(prompt)

    return article