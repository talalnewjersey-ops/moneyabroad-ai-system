from agents.utils.openai_client import generate_text 

def create_article(keyword, country):

    prompt = f"""
You are a finance expert for newcomers in {country}, writing for MoneyAbroadGuide.com.

Write a COMPLETE, HIGH-AUTHORITY, SEO-OPTIMIZED ARTICLE.

TARGET:
- 3000 to 3500 words
- Educational, structured, trustworthy (YMYL compliant)
- Audience: immigrants, expats, international students

TITLE:
"{keyword} in {country} (2026 Complete Guide)"

-----------------------------------
STRUCTURE (MANDATORY)
-----------------------------------

H1: Title

Author block:
- By Talal Eddaouahiri
- Expert in finance for newcomers (USA & Canada)
- Founder of MoneyAbroadGuide.com

Publish date + Last updated date

Disclaimer:
"This article is for educational purposes only and does not constitute financial advice."

-----------------------------------

INTRO (150 words)
- Problem newcomers face
- Why this guide matters

-----------------------------------

H2: What is this
(300 words)

H2: How it works
(400 words)

-----------------------------------

H2: Best options in {country}
- Real banks (RBC, TD, Scotiabank, CIBC, etc.)
- Pros / cons

-----------------------------------

H2: Comparison Table
Include:
| Bank | Monthly Fees | Requirements | Benefits | Best For |

-----------------------------------

H2: Visual Chart
Explain differences (fees, benefits, accessibility)

-----------------------------------

H2: Real-life stories (IMPORTANT)
Story 1: newcomer struggling with banking
Story 2: successful setup

-----------------------------------

H2: Why it matters for newcomers
(300 words)

-----------------------------------

H2: Common mistakes to avoid
(200 words)

-----------------------------------

H2: FAQ (5 questions)

-----------------------------------

H2: Conclusion
(150 words)

-----------------------------------

IMAGES (VERY IMPORTANT)
Add 4 realistic image placeholders like:

[Image: newcomer opening bank account in Canada]
[Image: comparison of banking options]
[Image: mobile banking app usage]
[Image: financial planning for immigrants]

-----------------------------------

SEO OPTIMIZATION

- Strong H1, H2, H3 structure
- Natural keyword usage
- Add internal linking suggestions (4 links)
- Add meta description (160 chars)

-----------------------------------

SCHEMA (IMPORTANT)

Include JSON-LD for:
- Article
- FAQ

-----------------------------------

STYLE

- Human tone (not robotic)
- Clear, simple English
- Helpful and trustworthy
- Avoid fluff

-----------------------------------

IMPORTANT

- This is NOT a blog post
- This is a PROFESSIONAL GUIDE
- Must feel like NerdWallet level content
"""

    return generate_text(prompt)