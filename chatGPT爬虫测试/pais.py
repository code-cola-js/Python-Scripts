# 这玩意可以爬一个静态页面

# Import the libraries
import requests
from bs4 import BeautifulSoup

# Define the URL to crawl
url = "https://www.hisea.com/"

# Make a GET request to the URL and get the response
response = requests.get(url)

print(response.status_code)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    print(response.content)
    # Parse the response content as HTML using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    print(soup)

    # Find all the elements with the class name "text"
    texts = soup.find_all(class_="text")

    # Loop through each element and print its text content
    for text in texts:
        print(text.get_text())
else:
    # Print an error message if the response status code is not 200
    print(f"Error: Could not access {url}")
