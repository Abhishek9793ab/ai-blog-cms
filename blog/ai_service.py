import json
import os

import requests


class AIServiceError(Exception):
    pass


def generate_blog_with_gemini(
    topic,
    keyword="",
    tone="professional",
    length="medium"
):

    api_key = os.getenv(
        "GEMINI_API_KEY",
        ""
    ).strip()

    model = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.6-flash"
    ).strip()


    if not api_key:

        raise AIServiceError(
            "GEMINI_API_KEY is not configured in .env file."
        )


    if not topic:

        raise AIServiceError(
            "Blog topic is required."
        )


    prompt = f"""
You are an expert SEO content writer.

Create a high-quality, original blog article.

Topic:
{topic}

Focus keyword:
{keyword or "Choose a natural primary keyword"}

Tone:
{tone}

Length:
{length}


Return ONLY valid JSON.

The JSON must contain exactly these keys:

title
excerpt
content_html
seo_title
meta_description
focus_keyword
tags


Requirements:

1. Create a professional SEO-friendly title.
2. Create a useful short excerpt.
3. Write a complete article.
4. content_html must use semantic HTML.
5. Use h2, h3, p, ul, ol and strong where useful.
6. Do not use Markdown.
7. Do not use code fences.
8. SEO title should preferably be 60 characters or less.
9. Meta description should preferably be 160 characters or less.
10. Focus keyword should naturally appear in the article.
11. tags must be a JSON array.
12. Content should be useful and readable.
13. Avoid unnecessary repetition.
14. Do not include any explanation outside JSON.
""".strip()


    url = (
        "https://generativelanguage.googleapis.com/"
        f"v1beta/models/{model}:generateContent"
    )


    payload = {

        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],

        "generationConfig": {

            "temperature": 0.7,

            "maxOutputTokens": 5000,

            "responseMimeType": "application/json",
        },
    }


    headers = {

        "x-goog-api-key": api_key,

        "Content-Type": "application/json",
    }


    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=90
        )

    except requests.RequestException as exc:

        raise AIServiceError(
            f"Gemini request failed: {exc}"
        ) from exc


    if not response.ok:

        try:
            detail = response.json()

        except ValueError:

            detail = response.text


        raise AIServiceError(
            f"Gemini API error "
            f"({response.status_code}): {detail}"
        )


    try:

        data = response.json()

    except ValueError as exc:

        raise AIServiceError(
            "Gemini returned an invalid response."
        ) from exc


    try:

        text = (
            data["candidates"][0]
            ["content"]
            ["parts"][0]
            ["text"]
        )

    except (
        KeyError,
        IndexError,
        TypeError
    ) as exc:

        raise AIServiceError(
            f"Unexpected Gemini response: {data}"
        ) from exc


    text = text.strip()


    # Remove accidental markdown fences
    if text.startswith("```"):

        text = text.replace(
            "```json",
            "",
            1
        )

        text = text.replace(
            "```",
            "",
            1
        )

        text = text.strip()


    try:

        result = json.loads(text)

    except json.JSONDecodeError as exc:

        raise AIServiceError(
            "Gemini returned invalid JSON. Please try again."
        ) from exc


    required_keys = [
        "title",
        "excerpt",
        "content_html",
        "seo_title",
        "meta_description",
        "focus_keyword",
        "tags",
    ]


    for key in required_keys:

        if key not in result:

            if key == "tags":
                result[key] = []

            else:
                result[key] = ""


    if not isinstance(
        result["tags"],
        list
    ):

        result["tags"] = [
            str(result["tags"])
        ]


    return result