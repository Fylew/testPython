import requests
import lxml
from bs4 import BeautifulSoup

def main_menu(): ### main menu ###
    print("Выберете пункт:\n1-Работа по списку id\n2-Работа по никнейму") # selecting the operating mode
    answer = int(input())
    if answer == 1:
        id_search()
    if answer == 2:
        nick_name_search()
    else:
        main_menu()

def id_search(): ###search from a given ip###

    num = int(input("Введите начальный id: "))
    for i in range(num, 1000000000000000, 1):
        generic = "id" + str(i)
        url = f"https://vk.com/{generic}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        print(soup.title.text, url)
        aa = soup.find_all("div", class_="OwnerInfo__rowCenter")
        for sity in aa:
            print(sity.text) ####output of text with information###

def nick_name_search(): ###search by name###

    nick = input("Введите никнейм: ")
    url = f"https://vk.com/{nick}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    print(soup.title.text, url)
    aa = soup.find_all("div", class_="OwnerInfo__rowCenter")
    for sity in aa:
        print(sity.text) ###output of text with information###
    main_menu()


main_menu()

