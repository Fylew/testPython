num_list_10 = {
    "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
    "десять": 10, "одинадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
    "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, "двадцать": 20, "тридцать": 30,
    "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90}


def prowerka(calc):
    flag = True
    num_1 = ""
    num_2 = ""
    for i in calc:
        if i == "разделить" or i == "умножить" or i == "минус" or i == "плюс":
            sym = calc.index(i)
            num_1 = calc[:sym]
            num_2 = calc[sym + 1:]
    for i in num_1:
        if i not in num_list_10:
            flag = False
    for i in num_2:
        if i not in num_list_10:
            flag = False
    return flag


def mainmenu():
    calculaor = input("Введите дейсвие: ")
    calculaor = calculaor.split()
    if prowerka(calculaor):
        calc(calculaor)
    else:
        print("Не корректный ввод")
        mainmenu()


def conclusion(num):
    out_1 = ""
    out_2 = ""
    if len(str(num)) > 1:

        num_2 = num % 10
        num_1 = num - num_2
        for k, v in num_list_10.items():
            if num_2 == v:
                out_1 += k
            elif num_1 == v:
                out_2 += k
        print(out_2 + ' ' + out_1)
    else:
        for k, v in num_list_10.items():
            if num == v:
                print(k)


def de(num):
    number = 0
    for i in num:
        if i in num_list_10:
            number += num_list_10[i]
    return number


def calc(cl):
    if "плюс" in cl:

        first_num = cl[:cl.index("плюс")]
        sec_num = cl[cl.index("плюс") + 1:]

        num = de(first_num) + de(sec_num)
        conclusion(num)

    elif "разделить" in cl:

        first_num = cl[:cl.index("разделить")]
        sec_num = cl[cl.index("разделить") + 1:]

        num = de(first_num) / de(sec_num)
        conclusion(num)

    elif "минус" in cl:
        first_num = cl[:cl.index("минус")]
        sec_num = cl[cl.index("минус") + 1:]

        num = de(first_num) - de(sec_num)
        conclusion(num)

    elif "умножить" in cl:
        first_num = cl[:cl.index("умножить")]
        sec_num = cl[cl.index("умножить") + 1:]

        num = de(first_num) * de(sec_num)
        conclusion(num)

    mainmenu()


mainmenu()