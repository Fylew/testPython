import tkinter as tk
import requests
import lxml
from bs4 import BeautifulSoup
from urllib.parse import quote
import random

word_out = []

word_counts = 0
w = ""
alf = ["абвгдеёжзийклмнопрстуфхцчшщъыьэюя"]

dikt = {}
word = open("DB","r")
for alfa in alf[0]:
    dikt[alfa]=[]

for i in word:
    i=i[:-1]

    dikt[i[0]].append(i)
def medium_game(word_in_game,ww,worde):

    global w
    global word_counts

    worde.delete(0, 'end')
    label1['text'] = "??????? ?????\n" \
                     "????? ??????? {} ????(?) ??? ??????!".format(49 - word_counts)

    if word_counts == 49:
        label1['text'] = "Вы Победили!!!"


    tail_word = game(word_in_game,ww)

    wordes(tail_word,ww)

    word_counts += 1


    medi()

def Hard_game(word_in_game,ww,worde): #challenging game level
    global w
    global word_counts

    worde.delete(0, 'end')
    label1['text'] = "??????? ?????\n" \
                     "????? ??????? {} ????(?) ??? ??????!".format(99 - word_counts)

    if word_counts == 99:
        label1['text'] = "?? ????????!!!"


    tail_word = game(word_in_game,ww)

    wordes(tail_word,ww)

    word_counts += 1
    hard()

def unreal_game(word_in_game,ww,worde): #endless game level
    global w
    global word_counts

    worde.delete(0, 'end')

    label1['text'] = "Безконечный режим\n" \
                     "Названно слов {}".format(word_counts)

    tail_word=game(word_in_game,ww)

    wordes(tail_word,ww)
    word_counts +=1
    unr()
def izi_game(word_in_game,ww,worde): #easy level of play
    global w
    global word_counts

    worde.delete(0, 'end')

    label1['text'] = "Простой режим \n" \
                     "Нужно назвать {} Слов(а) для победы!".format(24 - word_counts)
    if word_counts == 24:
        label1['text'] = "Ты победил!!!"


    tail_word=game(word_in_game,ww)

    wordes(tail_word,ww)

    word_counts += 1
    izi()

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

def wordes(tail_word,ww): #getting a list of words for the desired letter
    global w

    word = random.choice(dikt[tail_word])
    if word in word_out:
        word = random.choice(dikt[tail_word])

    if word[-1] == "?" or word[-1] == "?" or word[-1] == '?':
        w = word[-2]
        word_out.append(word)

    else:
        w = word[-1]
        word_out.append(word)
        ww["text"] = f"{word}, тебе на  {w} "

    word_out.append(word)


def game(word,ww): #The main part of the game, with word input
    global w

    print("-" * 74)
    word=word.lower()
    print(word)
    if word[0] != w and word_counts > 0:
        ww['text']=f"???, ????? ?????? ???? ?? ????? {w}"
        izi()

    elif word in word_out:
        ww['text']=f"Слово {word} Уже было!"
        izi()

    elif not check(word):
        ww['text']="Слово должно быть существительным"
        izi()

    tail_word = word[-1]

    if tail_word == "?" or tail_word == "?" or tail_word == "?":
        tail_word = word[-2]

    word_out.append(word)
    return tail_word

def izi():
    label1['text'] = "Простая игра\n" \
                     "Для победы нужно назвать {} слов(а)!".format(25)
    izi.destroy()
    medi.destroy()
    hard.destroy()
    unr.destroy()


    worde = tk.Entry(win)# ???????? ????? ?????
    worde.pack()
    ww = tk.Label(win,text="",font=('Arial',15,"bold"))
    ww.pack() # ???????? ?????? ?????? ? ?????????? ??? ?????? ???????
    but1 = tk.Button(win, text="Ввод", command=lambda: izi_game(worde.get(),ww,worde)) # ?????? ?????? ??? ????? ?????? ? ???????? ?????????
    but1.pack()
def medi():
    label1['text'] = "Средний режим\n" \
                     "Для победы нужно назвать {} слов(а)!".format(50)
    izi.destroy()
    medi.destroy()
    hard.destroy()
    unr.destroy()


    worde = tk.Entry(win)# ???????? ????? ?????
    worde.pack()
    worde.delete(0, 'end')
    ww = tk.Label(win, text="", font=('Arial', 15, "bold"))
    ww.pack()  # ???????? ?????? ?????? ? ?????????? ??? ?????? ???????
    but1 = tk.Button(win, text="Ввод",
                     command=lambda: medium_game(worde.get(), ww,worde))  # ?????? ?????? ??? ????? ?????? ? ???????? ?????????
    but1.pack()

def hard():
    label1['text'] = "Сложный режим\n" \
                     "Для победы нужно назвать {} слов(а)!".format(100)

    izi.destroy()
    medi.destroy()
    hard.destroy()
    unr.destroy()


    worde = tk.Entry(win)# ???????? ????? ?????
    worde.pack()
    ww = tk.Label(win, text="", font=('Arial', 15, "bold"))
    ww.pack()  # ???????? ?????? ?????? ? ?????????? ??? ?????? ???????
    but1 = tk.Button(win, text="Ввод",
                     command=lambda: Hard_game(worde.get(), ww,worde))  # ?????? ?????? ??? ????? ?????? ? ???????? ?????????
    but1.pack()
def unr():
    label1['text'] = "Безконечный режим"

    izi.destroy()
    medi.destroy()
    hard.destroy()
    unr.destroy()


    worde = tk.Entry(win)# ???????? ????? ?????
    worde.pack()
    ww = tk.Label(win, text="", font=('Arial', 15, "bold"))
    ww.pack()  # ???????? ?????? ?????? ? ?????????? ??? ?????? ???????
    but1 = tk.Button(win, text="Ввод",
                     command=lambda: unreal_game(worde.get(), ww,worde))  # ?????? ?????? ??? ????? ?????? ? ???????? ?????????
    but1.pack()

win = tk.Tk()
win.title("Word game v1.0")
win.geometry("550x300+600+250")

label1 = tk.Label(win, text="Игра в слова",
                  font=('Arial',20,"bold")
                  )
label1.pack()


izi = tk.Button(win,text="Простой режим",command=izi)
izi.pack()

medi = tk.Button(win,text="Средний режим",command=medi)
medi.pack()

hard = tk.Button(win,text="Сложный режим",command=hard)
hard.pack()

unr = tk.Button(win,text="Безконечный режим",command=unr)
unr.pack()

win.mainloop()