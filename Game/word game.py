import requests
import lxml
from bs4 import BeautifulSoup
from urllib.parse import quote
import random

word_out = [] #list of words used

word_counts = 0 #how many words are used
w = ""
alf = ["абвгдеёжзийклмнопрстуфхцчшщъыьэюя"]

word = open("DB.py","r")
dikt = {}
for alfa in alf[0]:
    dikt[alfa]=[]
for i in word:
    i=i[:-1]
    dikt[i[0]].append(i)
def check(word): #checking a word for a part of speech
    url = f"https://morphological.ru/{quote(word)}"#click on the link to the website
    response = requests.get(url)#getting the page code
    soup = BeautifulSoup(response.text, "lxml")
    aa = soup.find_all("table", class_="table table-bordered table-condensed table-striped")

#iterating through the code to find the desired section
    for i in aa:
        g = i.tbody.tr.text.split()
        for word in g:
            if word == "существительное":
                return True

        return False

def wordes(tail_word): #getting a list of words for the desired letter
    global w

    word = random.choice(dikt[tail_word])
    if word in word_out:
        word = random.choice(dikt[tail_word])
    print(word)

    if word[-1] == "ъ" or word[-1] == "ы" or word[-1] == 'ь':
        w = word[-2]
        word_out.append(word)
        print(f"Тебе на {w}")
    else:
        w = word[-1]
        word_out.append(word)
        print(f"Тебе на {w}")


def game(): #The main part of the game, with word input
    global w

    print("-" * 74)
    word = input("Введите слово: ").lower()

    if word[0] != w and word_counts > 0:
        print(f"Нет тебе надо на {w}")
        game()

    elif word in word_out:
        print(f"Слово {word} уже было ")
        game()

    elif not check(word):
        print("слово должно быть существительным!")
        game()

    tail_word = word[-1]

    if tail_word == "ь" or tail_word == "Ъ" or tail_word == "ы":
        tail_word = word[-2]

    word_out.append(word)
    return tail_word
def izi_game(*args): #easy level of play

    global w
    global word_counts

    if word_counts == 25:
        print("Вы победили!!!")
        exit()

    tail_word=game()

    wordes(tail_word)

    word_counts += 1
    print("До победы осталось {} слов".format(25 - word_counts))
    izi_game()


def medium_game(): #the average level of the game

    global w
    global word_counts

    if word_counts == 50:
        print("Вы победили!!!")
        exit()

    tail_word = game()

    wordes(tail_word)

    word_counts += 1
    print("До победы осталось {} слов".format(50- word_counts))
    medium_game()

def Hard_game(): #challenging game level
    global w
    global word_counts

    if word_counts == 100:
        print("Вы победили!!!")
        exit()

    tail_word = game()

    wordes(tail_word)

    word_counts += 1
    print("До победы осталось {} слов".format(100- word_counts))
    Hard_game()

def unreal_game(): #endless game level


    tail_word=game()

    wordes(tail_word)

    unreal_game()

def main_menu(): #Main Menu

    num = input("Выберете режим игры\n1-простой\n2-средний\n3-сложный\n4-не реальный!\n")

    if num == '1':
        print("-"*30,"Правила игры","-"*30)
        print("-"*20,"Для победы нужно набрать 25 балов!","-"*18)
        izi_game()

    elif num == '2':
        print("-"*30,"Правила игры","-"*30)
        print("-"*20,"Для победы нужно набрать 50 балов!","-"*18)
        medium_game()

    elif num == '3':
        print("-"*30,"Правила игры","-"*30)
        print("-"*20,"Для победы нужно набрать 100 балов!","-"*18)
        Hard_game()

    elif num == '4':
        print("-"*30,"Правила игры","-"*30)
        print("-"*25,"Здесь нельзя победить!","-"*25)
        unreal_game()

    else:
        print("Не корректный ввод!")
        main_menu()


main_menu()
