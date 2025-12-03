# -*- coding: utf-8 -*-
"""Lesson6.py

# Регулярні вирази та розширена робота з рядками
"""

import re

"""## Варіанти створення рядків


"""

this_is_string = "Hi there!"

the_same_string = 'Hi there!'

this_is_string == the_same_string

s = "Hello, світ\nNew line\tTabbed"          # звичайний рядок з escape-послідовностями
raw = r"C:\new\folder\file.txt"              # raw-рядок — не інтерпретує \n, \t
multi = """Багаторядковий
текст зі "лапками" і перенесеннями."""
print("s:"); print(s)
print("raw:", raw)
print("multi:", multi)

text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."

one_line_text

"""Неявна конкатенація рядків"""

query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")

"""## Спеціальні символи"""

print("1. Hello\nWorld")
print("2. Hello\tWorld")
print("3. Hello \r my World")
print("4. Hello\bWorld")
print("5. Hello\\World")

"""## Незмінність"""

s = "Hello, світ\nNew line\tTabbed"

try:
    s[0] = "h"
except TypeError as e:
    print("TypeError при спробі змінити символ:", e)

"""## Методи рядків"""

t = "  PyThOn 3.11  "
print("lower:", t.lower())
print("upper:", t.upper())
print("title:", "hello world".title())
print("capitalize:", "світ".capitalize())
print("strip:", t.strip(), "| lstrip:", t.lstrip(), "| rstrip:", t.rstrip(), "|")



u = "banana bandana"
print("count('ana') ->", u.count("ana"))

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end))
print(s.find("q"))

s = 'Some words'

print(s.find("o"))
print(s.rfind('o'))

s = 'Some words'

print(s.index("o"))
print(s.rindex('o'))

"""## Поділ та об'єднання рядків


"""

text = "hello world"
result = text.split()
print(result)

text = "apple,banana,cherry"
result = text.split(',')
print(result)

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)

clean = '   spacious   '.strip()
print(clean)

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text)

print('TestHook'.removeprefix('Test'))
print('TestHook'.removeprefix('Hook'))

print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))

number = "12345"
print(number.isdigit())

text = "Number123"
print(text.isdigit())

"""## Розширена обробка рядків: метод translate()"""

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab))

symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

result = "34 DF 56 AC".translate(MAP)
print(result)

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

result = "34 DF 56 AC".translate(MAP)
print(result)







morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)

table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)

"""## Форматування рядків"""

for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)

width = 5
for num in range(12):
    print(f'{num} {num**2:^20} {num**3:^20}')

"""<: Вирівнювання вмісту по лівому краю.
>: Вирівнювання вмісту по правому краю.
^: Вирівнювання вмісту по центру.
=: Використовується для вирівнювання чисел, при цьому знак (якщо він є) відображається зліва, а число - по правому краю поля.
"""

name = "Alice"
formatted = f"{name:>10}"
print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)

completion = 0.756
formatted = f"{completion:3.5f}"
print(formatted)  # Виведе: '75.6%'

name = "Oleksii"; score = 0.9876; n = 1_234_567; x = 42
print(f"Hi {name}, score={score:.2%}")            # відсотки з двома знаками
print(f"n з роздільником тисяч: {n:,}")           # 1,234,567
print(f"x у двійковій (08b): {x:08b}")            # 00101010
print("format() еквівалентно:", format(score, ".1%"))

"""## Регулярні вирази

https://www.programiz.com/python-programming/regex

`re.search(pattern, string)` - виконує пошук першого входження шаблону в рядку.

`re.findall(pattern, string)` - виконує знаходження всіх входжень шаблону в рядку.

`re.sub(pattern, repl, string)` - виконує заміну входжень шаблону на інший рядок.

`re.split(pattern, string)` виконує розбивання рядка за шаблоном.

`\w` — будь-яка цифра або буква [a-zA-Z0-9_] (`\W` — все, крім букви або цифри [^a-za-z0-9_])

`\d` — будь-яка цифра [0-9] (`\D` — усе, крім цифри [^0-9])

`\s` — будь-який пробільний символ [\t\n\r\f\v] (`\S` — усе, крім пробільних символів [^\t\n\r\f\v])

`\b` — межа слова

`[...]` — один із символів у дужках (`[^ ]` — будь-який символ, крім тих, що в дужках)

`^` і `$` — початок і кінець рядка відповідно

`( )` — групує вираз і повертає знайдений текст

`\t`, `\n`, `\r` — символ табуляції, нового рядка та повернення каретки


Модифікатори можуть вказувати на кількість повторень блоку у виразі, наприклад:

`.` — один будь-який символ, крім рядка \n

`?` — 0 або 1 входження шаблону зліва

`+` — 1 і більше входжень шаблону зліва

`*` — 0 і більше входжень шаблону зліва

`\` — екранування спеціальних символів (приклад: `\.` — означає крапку або `\+` — знак "плюс")

`{n}` суворо n разів (n ціле число)

`{n,m}` — від n до m входжень (приклад: {,m} — від 0 до m)

`a|b` — відповідає a або b. Сам символ | означає "або" між двома шаблонами

`( )` — групує вираз і повертає знайдений текст
"""



"""### `re.search`"""

text = "Вивчення Python може бути веселим."
pattern = "Python"
match_pattern = re.search(pattern, text)

if match_pattern:
    print("Знайдено:", match_pattern.group())
else:
    print("Не знайдено.")

type(match_pattern)

text = "Вивчення Python може бути веселим."
pattern = r"\w*я"
match_pattern = re.search(pattern, text, re.IGNORECASE)

if match_pattern:
    print("Знайдено:", match_pattern.group())

text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match_pattern = re.search(pattern, text)

if match_pattern:
    print("Електронна адреса:", match_pattern.group())

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match_pattern = re.search(pattern, email)

if match_pattern:
    user_name = match_pattern.group(1)
    domain_name = match_pattern.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)

"""### `re.findall`"""

s = "User_007, місто Kyiv!\nДата: 31-12-2025\tOK"

print(re.findall(r"\w+", s))                 # ['User_007', 'місто', 'Kyiv', 'Дата', '31', '12', '2025', 'OK']
print(re.findall(r"\d+", s))                 # ['007', '31', '12', '2025']
print(re.findall(r"\s+", s))                 # [', ', ' ', '!\n', ' ', '\t']
print(re.findall(r"\bKyiv\b", s))            # ['Kyiv']
print(re.findall(r"(\d{2})-(\d{2})-(\d{4})", s))  # [('31','12','2025')]
print(bool(re.fullmatch(r"\d+", "12345")))   # True (усе — цифри)
print(bool(re.fullmatch(r"\d+", "123a")))    # False

text = "Контакти: example1@example.com, example2@sample.org"
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)

print(matches)

"""### `re.sub`"""

file_name = "Мій документ Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(formatted_name)

text = "Python - потужна, універсальна; мова!"
pattern = r"[;,\-!\.]"
replacement = ""
modified_text = re.sub(pattern, replacement, text)

print(modified_text)

phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone)

"""### `re.split()`"""

text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)

print(fruits)