"""
Модуль считывает настройки файла "settings.txt"
"""

import gently_stop


try:
    with open('settings.txt', "r") as file:
        payload = file.readlines()

    for line in payload:
        if line.startswith("login"):
            login = line.split('"')[1]
        if line.startswith("password"):
            password = line.split('"')[1]
        if line.startswith("path"):
            path = line.split('"')[1]
        if line.startswith("file"):
            file = line.split('"')[1]
        if line.startswith("sheet"):
            sheet = line.split('"')[1]
        if line.startswith("url"):
            url = line.split('"')[1]
except FileNotFoundError:
    print("Не удается найти файл settings.txt в папке с приложением.")
    gently_stop.gently_stop_program()
    raise FileNotFoundError

# todo В будущем включить механизм затирания полей login и password для безопасности, чтобы их приходилось регулярно вводить заново

# for i in range(len(payload)):
#     if payload[i].startswith('sheet'):
#         payload[i] = "sheet : \"\" "
#         print(payload[i])
#
# file = open('settings.txt', 'w')
# file.writelines(payload)
# file.close()
