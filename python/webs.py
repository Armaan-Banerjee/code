import requests
import random


for i in range(30000):
    URLS = ["https://www.reddit.com", "https://www.google.com", "https://snake.io", "https://www.discord.com", "https://simpleflying.com", "https://code.visualstudio.com", "https://www.amazon.com", "https://aws.amazon.com", "https://www.reuteurs.com", "https://www.ft.com"]
    url = random.choice(URLS)
    x = requests.get(url)

print("done")
