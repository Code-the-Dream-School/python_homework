import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Load the search results page
    url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Find all search result items
    results = []
    items = driver.find_elements(By.CSS_SELECTOR, "li[class^='cp-search-result']")

    for item in items:
        # Extract title
        try:
            title_element = item.find_element(By.CSS_SELECTOR, "h2 a")
            title = title_element.text.strip()
        except:
            title = "N/A"

        # Extract authors
        try:
            author_elements = item.find_elements(By.CSS_SELECTOR, "a.author-link")
            authors = "; ".join([author.text.strip() for author in author_elements])
        except:
            authors = "N/A"

        # Extract format and year
        try:
            format_element = item.find_element(By.CSS_SELECTOR, "span.format")
            format_year = format_element.text.strip()
        except:
            format_year = "N/A"

        # Append the extracted data to the results list
        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        })

    # Create a DataFrame from the results
    df = pd.DataFrame(results)
    print(df)

    # Save to CSV and JSON
    df.to_csv("assignment9/get_books.csv", index=False)
    with open("assignment9/get_books.json", "w") as f:
        json.dump(results, f, indent=4)

finally:
    driver.quit()
