from agents.utils.openai_client import generate_text

def optimize_seo(article):

    prompt = f"""
    You are an SEO expert.

    Optimize this article for Google ranking.

    Requirements:
    - Strong H1, H2, H3 structure
    - Add meta description
    - Add FAQ section (3 questions)
    - Improve readability
    - Use keywords naturally
    - Add EEAT (experience, expertise, authority, trust)
    - Make it human and engaging

    Article:
    {article}
    """

    return generate_text(prompt)