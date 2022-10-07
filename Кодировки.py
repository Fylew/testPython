def mainMenu(): #Main Menu
    print("Выбор кодировки")
    code = int(input("Выберете номер желаемой кодировки:\n1-Шифир Виженера\n"))
    if code == 1:
        Venger()

    else:
        print("Не корректный ввод!")
        mainMenu()

def Venger(): #Function with encoding
    alf = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю','я']
    per = int(input("Выберете действие:\n1-шифровка\n2-расшифровка\n>>>  "))  #choosing an action encoding or decryption
    new_text = [] # new text after decryption
    if per == 1:
        tr = 0
        text = input("Введите текст для кодировки: ").lower()
        key = input("Введите ключ: ").lower()
        for i in text:

            if tr == len(key):
                tr = 0

            if i == " ":
                print(" ")
                new_text.append(" ")
                continue

            else:
                if alf.index(i) + alf.index(key[tr]) > 32:
                    new_index = abs(33 - (alf.index(i) + alf.index(key[tr])))

                else:
                    new_index = alf.index(i) + alf.index(key[tr])

            new_text.append(alf[new_index])
            tr += 1
        print("".join(new_text))
        mainMenu()

    elif per == 2:
        text = input("Введите текст для расшифровки: ").lower()
        key = input("Введите ключ: ").lower()
        new_text = []
        tr = 0
        for i in text:

            if tr == len(key):
                tr = 0

            if i == " ":
                print(" ")
                new_text.append(" ")
                continue

            else:
                if alf.index(i) + alf.index(key[tr]) < 0:
                    new_index = abs(33 - (alf.index(i) - alf.index(key[tr])))

                else:
                    new_index = alf.index(i) - alf.index(key[tr])

            new_text.append(alf[new_index])
            tr += 1
        print("".join(new_text))

mainMenu()