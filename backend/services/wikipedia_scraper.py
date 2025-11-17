import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class WikipediaScraperError(Exception):
    """Custom exception for Wikipedia scraping errors."""
    pass

def validate_wikipedia_url(url: str) -> bool:
    """Validate that the URL is a Wikipedia article URL."""
    try:
        parsed = urlparse(url)
        return ('wikipedia.org' in parsed.netloc and parsed.path.startswith('/wiki/'))
    except Exception:
        return False

def extract_article_content(url: str) -> dict:
    """Fetch and extract the main content of a Wikipedia article."""
    if not validate_wikipedia_url(url):
        raise WikipediaScraperError("Invalid Wikipedia URL provided.")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Extract title
        title_tag = soup.find("h1", id="firstHeading")
        title = title_tag.text.strip() if title_tag else "Unknown Title"

        # Extract main content
        content_div = soup.find("div", class_="mw-content-ltr mw-parser-output")
        if not content_div:
            raise WikipediaScraperError("Could not find article content.")

        # Remove unwanted tags
        for tag in content_div.find_all(["script", "style", "sup", "table", "img"]):
            tag.decompose()

        # Extract text from paragraphs
        paragraphs = []
        for element in content_div.find_all("p", recursive=False):
            text = element.get_text(strip=True)
            if len(text) >= 30:  # Require longer content to avoid stub articles
                paragraphs.append(text)

        if len(paragraphs) < 1:
            raise WikipediaScraperError("Not enough article content found.")

        # Join and truncate to avoid very long output
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
