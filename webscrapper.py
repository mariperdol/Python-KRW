# Repository: python-web-scraper
# Description: Scrape data from websites using BeautifulSoup.

import requests
from bs4 import BeautifulSoup

import json

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = [{"paragraph": p.text} for p in soup.find_all('p')]
    with open('scraped_data.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Data exported to scraped_data.json")
# Example usage
scrape_website("https://example.com")
