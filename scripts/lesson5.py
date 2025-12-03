# -*- coding: utf-8 -*-
"""
**Algorithms + Data Structures = Programs**

 is a 1976 book written by Niklaus Wirth covering some of the fundamental topics of system engineering, computer programming, particularly that algorithms and data structures are inherently related.


 **Дані**

 змінні (int, float, str, boolean)

 структури даних (list, dict, set, tuple)



 **Алгоритми**

 if, match, for, while

 вбудовані функції

 (https://docs.python.org/3/library/functions.html)

 бібліотечні функції
"""

import keyword


print(f"Всього ключових слів: {len(keyword.kwlist)}")
print(keyword.kwlist)

"""# Робота з випадковими величинами

## randint
"""

import random

random.randint(1, 1000)

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

"""## random"""

num = random.random()
print(num)



"""## randrange"""

print(random.randrange(10))  # Верхня межа є 10, але не включається

target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

"""## shuffle"""

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

random.shuffle(cards)

print(f"Перемішана колода: {cards}")

"""## choice"""

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item)

"""## sample"""

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")



"""`random.randint(a, b)`. Отримання випадкового цілого числа з рівномірного розподілу в інтервалі між a та b включно.

`random.random()`. Отримання випадкового числа в інтервалі між 0.0 (включно) та 1.0 (не включно).

`random.randrange(start, stop[, step])`. Отримання випадкового числа із заданого діапазону з можливістю вказати крок між значеннями.

`random.shuffle(x)`. Перемішування порядку елементів у списку x.

`random.choice(seq)`. Вибір випадкового елемента з послідовності seq (списку або кортежу).

`random.choices(population, weights=None, cum_weights=None, k=1)`. Генерація випадкової вибірки з можливістю зазначити ймовірності для кожного елемента та повторення у вибірці.

`random.sample(population, k)`. Отримання унікальних випадкових елементів зі списку population довжиною k.
random.uniform(a, b): Отримання випадкового дійсного числа N, такого, що a <= N <= b.
"""





"""# Математичні функції та операції"""

import math

math.pi

math.e

math.tau

math.inf

math.nan

import math

# Вихідне число
x = 3.7

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result)

math.pow(2, 3)

math.sqrt(16)

"""## порівняння дійсних чисел"""

import math

r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # Це поверне True

"""# Часові операції у програмуванні



"""

import datetime
from datetime import timezone, timedelta
import time

now = datetime.datetime.now()
print(now)



current_datetime = datetime.datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

current_datetime = datetime.datetime.now()
print(current_datetime.date())
print(current_datetime.time())

print(type(current_datetime))
print(type(current_datetime.date()))

print(str(current_datetime.date()))



# import datetime

# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

# Створення об'єкта datetime
now = datetime.datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")

# Створення двох об'єктів datetime
datetime1 = datetime.datetime(2023, 3, 14, 12, 0)
datetime2 = datetime.datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

"""## Часові проміжки"""

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

seventh_day_2019 = datetime.datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime.datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

seventh_day_2020 = datetime.datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

"""## Робота з timestamp"""

# Поточний час
now = datetime.datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу

# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime

"""## Парсинг дати із рядка

%Y - рік з чотирма цифрами (наприклад, 2023).

%y - рік з двома цифрами (наприклад, 23).

%m - місяць як номер (наприклад, 03 для березня).

%d - день місяця як номер (наприклад, 14).

%H - година (24-годинний формат) (наприклад, 15).

%I - година (12-годинний формат) (наприклад, 03).

%M - хвилини (наприклад, 05).

%S - секунди (наприклад, 09).

%A - повна назва дня тижня (наприклад, Tuesday).

%a - скорочена назва дня тижня (наприклад, Tue).

%B - повна назва місяця (наприклад, March).

%b або %h - скорочена назва місяця (наприклад, Mar).

%p - AM або PM для 12-годинного формату.
"""

now = datetime.datetime.now()

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)

# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу

"""## Робота з ISO форматом дати"""

# Поточна дата та час
now = datetime.datetime.now()

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)

iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.datetime.fromisoformat(iso_date_string)
print(date_from_iso)

# Створення об'єкта datetime
now = datetime.datetime.now()

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

# Створення об'єкта datetime
now = datetime.datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

"""## Робота з часовими зонами"""

local_now = datetime.datetime.now()
utc_now = datetime.datetime.now(timezone.utc)

print(local_now)
print(utc_now)  # Виведе поточний час в UTC

utc_time = datetime.datetime.now(timezone.utc)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime.datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime.datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)

"""## Робота з часом"""

current_time = time.time()
print(f"Поточний час: {current_time}")

import time

print("Початок паузи")
time.sleep(5)
print("Кінець паузи")

current_time = time.time()
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

"""## Лічильник часу"""

# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")