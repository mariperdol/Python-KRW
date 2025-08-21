from selenium import webdriver

def scrape_dynamic_website(url):
    driver = webdriver.Chrome()  # Убедитесь, что ChromeDriver установлен
    driver.get(url)
    content = driver.page_source
    print(content)
    driver.quit()

# Example usage
scrape_dynamic_website("https://example.com")
