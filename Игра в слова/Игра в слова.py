import requests
import lxml
from bs4 import BeautifulSoup
from urllib.parse import quote

word_out = []

word_counts = 0
w = ""

def check(word):
    url = f"https://morphological.ru/{quote(word)}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    aa = soup.find_all("table", class_="table table-bordered table-condensed table-striped")

    for i in aa:
        g = i.tbody.tr.text.split()
        for word in g:
            if word == "существительное":
                return True

        return False

def wordes(tail_word):
    global w
    url = f"http://www.reright.ru/words/{quote(tail_word)}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    aa = soup.find_all("div", class_="col-md-3 col-sm-3 col-xs-6")

    for i in aa:

        word_i = i.text
        if word_i in word_out:
            continue
        else:
            if check(word_i):
                print(word_i)
                word_out.append(word_i)

                if word_i[-1] == 'ъ' or word_i[-1] == 'ь' or word_i[-1] == 'ы':
                    print(f"Тебе на {word_i[-2]}")
                    w = word_i[-2]

                else:
                    print(f"Тебе на {word_i[-1]}")
                    w = word_i[-1]


            else:
                word_out.append(word_i)
                wordes(tail_word)
        return
def game():
    print("-"*74)
    word = input("Введите слово: ").lower()
    if check(word):
        if word[0] != w and word_counts >0:
            print(f"Нет тебе надо на {w}")
            game()

        elif word in word_out:
            print(f"Слово {word} уже было ")
            game()
    else:
        print("слово должно быть существительным!")
        game()
    tail_word = word[-1]

    if tail_word == "ь" or tail_word == "Ъ" or tail_word == "ы":
        tail_word = word[-2]

    return word,tail_word

def izi_game(*args):

    global w
    global word_counts

    if word_counts == 25:
        print("Вы победили!!!")
        exit()

    word,tail_word=game()

    word_out.append(word)

    wordes(tail_word)

    word_counts += 1
    izi_game()


def medium_game():

    global w
    global word_counts

    if word_counts == 50:
        print("Вы победили!!!")
        exit()

    word, tail_word = game()

    wordes(tail_word)

    word_counts += 1
    medium_game()

def Hard_game():
    global w
    global word_counts

    if word_counts == 100:
        print("Вы победили!!!")
        exit()

    word, tail_word = game()

    wordes(tail_word)

    word_counts += 1

    Hard_game()

def unreal_game():


    word,tail_word=game()

    wordes(tail_word)

    unreal_game()

def main_menu():

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
