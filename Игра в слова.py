import requests
import lxml
from bs4 import BeautifulSoup
words = {
    "а":"90",
    "б":"91",
    "в":"92",
    "г":"93",
    "д":"94",
    "е":"95",
    "ё":"81",
    "ж":"96",
    "з":"97",
    "и":"98",
    "й":"99",
    "к":"9A",
    "л":"9B",
    "м":"9C",
    "н":"9D",
    "о":"9E",
    "п":"9F",
    "р":"A0",
    "с":"A1",
    "т":"A2",
    "у":"A3",
    "ф":"A4",
    "х":"A5",
    "ц":"A6",
    "ч":"A7",
    "ш":"A8",
    "щ":"A9",
    "э":"AD",
    "ю":"AE",
    "я":"AF",
    "ы":"AB",
}
word_out = []

word_counts = 0
w = ""
def izi_game(*args):
    global words
    global word_counts
    global w

    if word_counts == 25:
        print("Вы победили!!!")
        exit()
    if word_counts > 0:
        word = input("Введите слово: ")
        word = word.lower()
        if word[:1:] != w:
            print(f"Неееет тебе надо на {w}")
            izi_game()

    if word_counts == 0:
        word = input("Введите слово: ")
        word = word.lower()

    if word in word_out:
        print(f"Слово {word} уже было ")
        izi_game()

    tail_word = word[-1]

    if tail_word == "ь" or tail_word == "Ъ" or tail_word == "ы":
        tail_word = word[-2]

    word_out.append(word)
    url = f"http://www.reright.ru/words/%D0%{words[tail_word]}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    aa = soup.find_all("div", class_="col-md-3 col-sm-3 col-xs-6")

    for i in aa:

        word_i = i.text

        if word_i in word_out:
            print("слово есть !")

        if word_i not in word_out:
            print(word_i)
            word_out.append(word_i)

            if word_i[-1] == 'ъ' or word_i[-1] == 'ь' or word_i[-1] == 'ы':
                print(f"Тебе на {word_i[-2]}")
                w = word_i[-2]

            else:
                print(f"Тебе на {word_i[-1]}")
                w = word_i[-1]

            izi_game()
            word_counts += 1


def medium_game():
    global words
    global word_counts

    if word_counts == 50:
        print("Вы победили!!!")
        exit()

    word = input("Введите слово: ")
    word = word.lower()

    if word in word_out:
        print(f"Слово {word} уже было ")
        izi_game()

    tail_word = word[-1]

    if tail_word == "ь" or tail_word == "Ъ" or tail_word == "ы":
        tail_word = word[-2]

    word_out.append(word)
    url = f"http://www.reright.ru/words/%D0%{words[tail_word]}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    aa = soup.find_all("div", class_="col-md-3 col-sm-3 col-xs-6")

    for i in aa:
        word_i = i.text

        if word_i in word_out:
            print("слово есть !")

        if word_i not in word_out:
            print(word_i)
            word_out.append(word_i)

            if word_i[-1] == 'ъ' or word_i[-1] == 'ь' or word_i[-1] == 'ы':
                print(f"Тебе на {word_i[-2]}")

            else:
                print(f"Тебе на {word_i[-1]}")
            word_counts += 1
            medium_game()

def Hard_game():
    global words
    global word_counts

    if word_counts == 100:
        print("Вы победили!!!")
        exit()

    word = input("Введите слово: ")
    word = word.lower()

    if word in word_out:
        print(f"Слово {word} уже было ")
        izi_game()

    tail_word = word[-1]
    if tail_word == "ь" or tail_word == "Ъ" or tail_word == "ы":
        tail_word = word[-2]

    word_out.append(word)
    url = f"http://www.reright.ru/words/%D0%{words[tail_word]}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    aa = soup.find_all("div", class_="col-md-3 col-sm-3 col-xs-6")

    for i in aa:
        word_i = i.text

        if word_i in word_out:
            print("слово есть !")

        if word_i not in word_out:
            print(word_i)
            word_out.append(word_i)

            if word_i[-1] == 'ъ' or word_i[-1] == 'ь' or word_i[-1] == 'ы':
                print(f"Тебе на {word_i[-2]}")

            else:
                print(f"Тебе на {word_i[-1]}")
            word_counts += 1
            Hard_game()

def unreal_game():
    global words
    word = input("Введите слово: ")
    word = word.lower()

    if word in word_out:
        print(f"Слово {word} уже было ")
        izi_game()

    tail_word = word[-1]

    if tail_word == "ь" or tail_word == "Ъ" or tail_word == "ы":
        tail_word = word[-2]

    word_out.append(word)
    url = f"http://www.reright.ru/words/%D0%{words[tail_word]}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    aa = soup.find_all("div", class_="col-md-3 col-sm-3 col-xs-6")

    for i in aa:
        word_i = i.text

        if word_i in word_out:
            print("слово есть !")

        if word_i not in word_out:
            print(word_i)
            word_out.append(word_i)

            if word_i[-1] == 'ъ' or word_i[-1] == 'ь' or word_i[-1] == 'ы':
                print(f"Тебе на {word_i[-2]}")

            else:
                print(f"Тебе на {word_i[-1]}")

            unreal_game()

def main_menu():

    num = input("Выберете режим игры\n1-простой\n2-средний\n3-сложный\n4-не реальный!\n")

    if num == '1':
        izi_game()

    elif num == '2':
        main_menu()

    elif num == '3':
        Hard_game()

    elif num == '4':
        unreal_game()

    else:
        print("Не корректный ввод!")
        main_menu()


main_menu()

