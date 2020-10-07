import openpyxl
from datetime import datetime, timedelta
from request import *
import time

# с каким файлом надо работать
FILE = "excel.xlsx"

# c каким листом надо работать
SHEET_NAME = "2020"


def datetime_to_excel_format_date(date):
    """Возвращает дату в формате Excel"""
    return datetime.strftime(date, "%d.%m.%Y")


def datetime_to_excel_format_time(date):
    """Возвращает время в формате Excel"""
    return datetime.strftime(date, "%H:%M:%S")


def rounded_to_4_hour_and_date(mydatetime: datetime):
    """Принимает datetime.
    Если текущее время больше чем на 2 часа, чем последнее контрольное, то
    округляет до следующего контрольного времени.
    Если текущее время больше 22 часов, округляет время до 0 часов, но прибавляет к дате 1 день.
    Возвращает данные в формате datetime  ГГГГ-ММ-ДД ЧЧ:ММ:СС"""

    hours = [0, 4, 8, 12, 16, 20, 0]

    mydatetime_hour = mydatetime.timetuple().tm_hour
    mydatetime_min = mydatetime.timetuple().tm_min / 60

    for hour in hours:
        if mydatetime_hour not in range(hour, hour + 4):
            continue
        else:
            if (mydatetime_hour + mydatetime_min - hour) <= 2:
                return mydatetime.replace(hour=hour, minute=0, second=0, microsecond=0)
            else:
                if mydatetime_hour + mydatetime_min > 22:
                    mydatetime_hour = hours[int(f'{hours.index(hour) + 1}')]
                    return (mydatetime + timedelta(days=1)).replace(hour=mydatetime_hour, minute=0, second=0,
                                                                    microsecond=0)
                else:
                    mydatetime_hour = hours[int(f'{hours.index(hour) + 1}')]
                    return mydatetime.replace(hour=mydatetime_hour, minute=0, second=0, microsecond=0)


def rounded_hour(mydatetime: datetime):
    """Округляет переданное время до целых часов."""
    if mydatetime.timetuple().tm_min == 59:
        mydatetime_hour = mydatetime.timetuple().tm_hour
        return mydatetime.replace(hour=mydatetime_hour+1, minute=0, second=0, microsecond=0)
    else:
        return mydatetime


def write_a_row_to_excel(heat_object):
    """Делает запись в эксель файле в строку с текущим mark-kow"""
    colls_list = ['I', 'L', 'N', 'O', 'P', 'R', 'U']

    params_list = [
        heat_object.ta,
        heat_object.t1,
        heat_object.t2,
        heat_object.p1,
        heat_object.p2,
        heat_object.g1,
        heat_object.gp_calc
    ]

    if heat_object.gp is not None:                          # проверка на наличие определенного прибором gp
        params_list.append(heat_object.gp)
        colls_list.append('T')

    for i in range(0, len(params_list)):
        ws[f'{colls_list[i]}{mark_row}'].value = params_list[i]


# даты в экселе сохранены в datetime
# время в экселе сохранено в виде datetime.time


# имитация даты 03.10.2020 18:28:00
# day = datetime(2020, 10, 3, 0, 0, 0).date()
# hour = datetime(year=1, day=1, month=1, hour=12, minute=11)
# rounded_to_4_hour = rounded_to_4_hour_and_date(hour)

day = datetime.now().date()
rounded_to_4_hour = rounded_to_4_hour_and_date(datetime.now())

print(f"Дата {day}")
print(f"Данные будут записаны в блок времени {rounded_to_4_hour.time()}")

wb = openpyxl.load_workbook(FILE, data_only=True)
ws = wb[SHEET_NAME]

mark_row = 0

try:
    # ищем блок с нужной датой и временем и сохраняем номер его строки
    for i in range(2, len(list(ws['D'])) + 1):
        cell_date = ws[f'D{i}'].value
        cell_hour = ws[f'E{i}'].value
        if cell_date.date() == day:
            if (rounded_hour(cell_hour).time() == rounded_to_4_hour.time()) or (cell_hour == rounded_to_4_hour.time()):
                mark_row = i
                break

    else:
        print("Дата не найдена")

    print(f'Запись будет сделана начиная с {mark_row} строки.')

    wb.close()

    # повторно открываем файл для записи данных
    wb = openpyxl.load_workbook(FILE)
    ws = wb[SHEET_NAME]

    names_of_epmty_sourses = [
        'hf_rts_150',
        "hf_kts_gornaya",
        "sf_mk_polet"
    ]

    for i in range(len(souses_list)):
        if souses_list[i].name not in names_of_epmty_sourses:           # проверка не подключенные источники
            write_a_row_to_excel(souses_list[i])
        mark_row += 1

    wb.save(FILE)
    wb.close()

    input("Нажми Enter для выхода.")
    print()
    print('        ++ Перед повторным запуском скрипта пересохрани файл в Excel ++')
    print()
    input("Повторно нажми Enter для выхода.")
except AttributeError:
    print()
    print()
    print("   ++ Нет кэшированных результатов вычисления формул. Откройте файл в Excel и пересохраните.  ++   ")
    print("                             ++ Затем заупстите скрипт заново  ++   ")
    print()
    print()
    input("Нажми Enter для выхода.")


