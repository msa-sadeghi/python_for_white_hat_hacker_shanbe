# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# url = input("enter site address: ")
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# links = set()
# for a in soup.find_all('a'):
#     link = urljoin(url, a['href'])
#     links.add(link)
# print("links are:")
# for l in links:
#     print(l)

# for h1 in soup.find_all('h2'):
#     print(h1.text)


from telegram import Bot
from telegram.utils.request import Request
token = '7988846919:AAH-uYRiA2NAg_8G4BTZBiMPAk6XcZUk8Kg'
chat_id = 360755066

request = Request(proxy_url="https://t.me/proxy?server=36.138.100.184&port=23071&secret=ee479662c147fb1859c24549155e75c4a16177732e616d617a6f6e2e636f6d")

bot = Bot(token=token, request=request)

bot.send_message(chat_id=chat_id,text="slaam")