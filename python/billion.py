import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/world-population/"

response = requests.get(URL, timeout=100)
soup = BeautifulSoup(response.content, "html.parser")
result = soup.find_all("span", "rts-counter")
print(result[0])
