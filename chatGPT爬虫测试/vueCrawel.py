# Import the libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Define the URL to crawl
url = "https://chuanyehedao.com/#/Practise?id=e3c21baa5d6b48d28c6dc3c9716c5f24&yearId=b6db53ba08b94c21b882eab723ad277f&headline=%3C%E8%80%83%E7%A0%94%E8%8B%B1%E8%AF%AD%E4%B8%80%3E%C2%B72010&isFree=0&name=%E9%98%85%E8%AF%BB1"

# Create a webdriver object for Chrome
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Wait for 10 seconds to let the page load
time.sleep(10)

# Get the HTML content of the page
html = driver.page_source

print(html)

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Find all the elements with the class name "text"
texts = soup.find_all(class_="text")

# Loop through each element and print its text content
for text in texts:
    print(text.get_text())

# Close the browser
driver.quit()
