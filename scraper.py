# scraper.py
import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove common non-content tags
        for tag in soup(["script", "style", "header", "footer", "nav", "aside", "form", "img"]):
            tag.decompose()

        # Extract text from meaningful elements
        elements = soup.find_all(['h1', 'h2', 'h3', 'p', 'li'])
        content = "\n".join([element.get_text(strip=True) for element in elements if element.get_text(strip=True)])

        return content

    except Exception as e:
        return f"Error fetching content: {e}"
