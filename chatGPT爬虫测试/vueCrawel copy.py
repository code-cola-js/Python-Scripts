# Import the libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Define the URL to crawl
url = "https://www.hisea.com/faqs"

# Create a webdriver object for Chrome
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Wait for 10 seconds to let the page load
time.sleep(10)

# Get the HTML content of the page
html = driver.page_source

html = html.replace('\xa0', ' ')
html = html.replace('\xa9', ' ')
print(html)

# 将html写入html.txt
with open('html.txt', 'w', encoding='utf-8') as f:
    f.write(html)


# Close the browser
driver.quit()
