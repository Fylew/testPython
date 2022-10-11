import requests
import lxml
from bs4 import BeautifulSoup
from urllib.parse import quote
import time
from tqdm import tqdm
import re
word_list = []
alf = ["абвгдеёжзийклмнопрстуфхцчшщъыьэюя"]

for word in tqdm(alf[0]):
    for num in tqdm(range(30)):
        if num >0:
            url = fr"https://wordsonline.ru/{quote(word.title())}?page={num}"
        else:
            url = fr"https://wordsonline.ru/{quote(word.title())}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        aa = soup.find_all("ul", class_="list-unstyled list-columns list-words")
        for i in aa:
            for g in i:
                if g == " ":
                    continue
                else:
                    word_list.append(g.text)
        time.sleep(1)
    time.sleep(1)

print(len(word_list))
f = open("WordBase.txt", "w")
for i in tqdm(word_list):
    f.write(i + "\n")
    time.sleep(1)