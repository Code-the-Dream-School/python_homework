from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import json
import os

options = webdriver.FirefoxOptions()
options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox"
# options.add_argument('--headless')  # Enable if needed

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

try:
    url = "https://owasp.org/www-project-top-ten/"
    driver.get(url)

    # Wait is optional here but can be added if needed
    elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/www-project-top-ten/20')]")

    results = []
    for el in elements:
        title = el.text.strip()
        href = el.get_attribute("href")
        if title:  # skip empty links
            results.append({"Title": title, "Link": href})

    print(results)

    # Save to CSV
    df = pd.DataFrame(results)
    df.to_csv("owasp_top_10.csv", index=False)
    print("Data saved to owasp_top_10.csv")

finally:
    driver.quit()
