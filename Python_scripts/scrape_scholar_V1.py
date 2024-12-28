from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# Set up Selenium WebDriver (you'll need ChromeDriver installed)
service = Service("path/to/chromedriver")  # Replace with the path to ChromeDriver
driver = webdriver.Chrome(service=service)

# Open the Google Scholar profile
url = "https://scholar.google.de/citations?view_op=list_works&hl=en&hl=en&user=sli-Dy4AAAAJ&sortby=pubdate"
driver.get(url)

time.sleep(5)  # Allow time for the page to load

# Extract publication details
publications = []
rows = driver.find_elements(By.CSS_SELECTOR, ".gsc_a_tr")
for row in rows:
    title = row.find_element(By.CSS_SELECTOR, ".gsc_a_at").text
    authors = row.find_elements(By.CSS_SELECTOR, ".gs_gray")[0].text
    publication_details = row.find_elements(By.CSS_SELECTOR, ".gs_gray")[1].text
    year = row.find_element(By.CSS_SELECTOR, ".gsc_a_y span").text
    publications.append({
        "Title": title,
        "Authors": authors,
        "Publication Details": publication_details,
        "Year": year,
    })

# Save to CSV
csv_file = r"C:\Users\osho799e\Lab_WebPage\test\publications.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Authors", "Publication Details", "Year"])
    writer.writeheader()
    writer.writerows(publications)

print(f"Publications exported to {csv_file}")

# Close the browser
driver.quit()
