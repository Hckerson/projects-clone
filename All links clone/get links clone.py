import requests as rq
from bs4 import BeautifulSoup
import os

url = input("Enter url (e.g., google.com or https://www.google.com) \n")
savePath = os.path.join(os.path.dirname(__file__), "../data.txt")

if not (url.startswith("https://") or url.startswith("http://")):
  url = f"https://{url}"

try:
  data = rq.get(url)
  data.raise_for_status()
except rq.exceptions.RequestException as e:
  print(f"An error occured {e}")
  exit()

soup = BeautifulSoup(data.text, "html.parser")
links = []

for link in soup.find_all("a"):
  links.append(link.get("href"))

with open('../mix.txt', "a") as saved:
  print(links[:10], file=saved)