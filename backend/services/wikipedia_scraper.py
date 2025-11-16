import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

class WikipediaScraperError(Exception):
    pass

def validate_wikipedia_url(url: str) -> bool:
    """Validate that the URL is a Wikipedia article URL"""
    try:
        parsed = urlparse(url)
        return "wikipedia.org" in parsed.netloc and "/wiki/" in parsed.path
    except:
        return False

def extract_article_content(url: str) -> dict:
    if not validate_wikipedia_url(url):
        raise WikipediaScraperError("Invalid Wikipedia URL provided")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Extract title
        title_tag = soup.find("h1", id="firstHeading")
        title = title_tag.text if title_tag else "Unknown Title"

        # Extract content
        content_div = soup.find("div", class_="mw-parser-output")
        if not content_div:
            raise WikipediaScraperError("Could not find article content")

        # Remove unwanted tags
        for tag in content_div(["script", "style", "sup", "table"]):
            tag.decompose()

        # Extract only real text paragraphs
        paragraphs = []
        for element in content_div.find_all(["p", "li"]):
            text = element.get_text(strip=True)
            if len(text) < 10:
                continue
            paragraphs.append(text)

        if len(paragraphs) < 1:
            raise WikipediaScraperError("Not enough article content found")

        content = "\n\n".join(paragraphs)[:4000]


        return {
            "title": title,
            "content": content,
            "url": url
        }

    except requests.RequestException as e:
        raise WikipediaScraperError(f"Failed to fetch Wikipedia page: {str(e)}")

    except Exception as e:
        raise WikipediaScraperError(f"Error processing Wikipedia page: {str(e)}")
