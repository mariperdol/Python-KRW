### **Repository 7: Web Scraper**
```python
# Repository: python-web-scraper
# Description: Scrape data from websites using BeautifulSoup.

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrape the title and content of a website."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else "No Title"
    paragraphs = [p.text for p in soup.find_all('p')]
    print(f"Title: {title}\nContent:\n{' '.join(paragraphs)}")

# Example usage
scrape_website("https://example.com")
