# Repository: python-web-scraper
# New Feature: Scrape multiple pages of a website

import requests
from bs4 import BeautifulSoup

def scrape_multiple_pages(base_url, pages=3):
    """Scrape content from multiple pages."""
    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Content from page {page}:")
        for p in soup.find_all('p'):
            print(p.text)
import requests

proxies = {
    "http": "http://proxy.example.com:8080",
    "https": "https://proxy.example.com:8080",
}

def scrape_website(url):
    response = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.title.string)

# Example usage
scrape_website("https://example.com")
# Example usage
scrape_multiple_pages("https://example.com/articles", pages=3)
