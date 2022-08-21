#!/usr/bin/python3

## Run selenium and chrome driver to scrape data
from lib2to3.pgen2 import driver
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Fetch web page
driver.get('https://YOUR_URL')

# Get web page url and title
print("Current URL: ", driver.current_url)
print("Webpage Title: ", driver.title, "\n")

# Extract links from page and print
links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
        print(link.get_attribute("href"))

driver.quit()

