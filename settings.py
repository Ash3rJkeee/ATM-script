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
    gently_stop.gently_stop_program(1)

