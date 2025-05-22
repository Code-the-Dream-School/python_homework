import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

import os

firefox_path = "/Applications/Firefox.app/Contents/MacOS/firefox"
if not os.path.exists(firefox_path):
    raise Exception("Firefox not found at expected path.")

options = webdriver.FirefoxOptions()
options.binary_location = firefox_path  # explicitly set Firefox path
#options.add_argument('--headless')  # Uncomment this line to run in headless mode

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

try:
    # Load the search results page
    url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    driver.get(url)
    #time.sleep(10)  # Wait for the page to load
    # Use WebDriverWait instead of sleep

    wait = WebDriverWait(driver, 20)
    items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.cp-search-result-item")))

    # Find all search result items
    results = []
    #items = driver.find_elements(By.CSS_SELECTOR, "li[class^='cp-search-result']")

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

    print(f"Scraped {len(results)} book entries.")
    print("Data saved to get_books.csv and get_books.json")


    # Save to CSV and JSON

    df.to_csv("get_books.csv", index=False)
    with open("get_books.json", "w") as f:
        json.dump(results, f, indent=4)

finally:
    driver.quit()
