### **Repository 7: Web Scraper**
```python
# Repository: python-web-scraper
# Description: Scrape data from websites using BeautifulSoup.

import requests
from bs4 import BeautifulSoup

def scrape_website(url, pages=1):
    for page in range(1, pages + 1):
        response = requests.get(f"{url}?page={page}")
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Page {page}:")
        for p in soup.find_all('p'):
            print(p.text)
# Example usage
scrape_website("https://example.com")
