# -*- coding: utf-8 -*-
"""Lesson9

# Модуль `collections`

https://docs.python.org/3/library/collections.html

Модуль `collections` надає спеціалізовані типи контейнерів, які є альтернативою стандартним вбудованим контейнерам Python (`dict`, `list`, `set`, `tuple`).

**Основні компоненти**

1.  **`namedtuple`** кортежі з іменованими полями.
2.  **`Counter`** інструмент для підрахунку хешованих об'єктів.
3.  **`defaultdict`** словник, який викликає фабричну функцію для відсутніх ключів.
4.  **`deque`** двостороння черга (ефективна для додавання/видалення з країв).

Додатково

5.  **`OrderedDict`** словник, що запам'ятовує порядок додавання записів (має специфічні методи для перевпорядкування).
6.  **`ChainMap`** клас для об'єднання кількох словників в одне віртуальне відображення.

# Іменовані кортежі

https://clawshea.medium.com/exploring-pythons-namedtuples-a-comprehensive-tutorial-84bdd45fcaa1

* `namedtuple` — це як звичайний кортеж, але з іменами полів.

* Доступ до елементів не тільки за індексом (p[0]), а й за ім’ям (p.x).


**Переваги**

* Читабельність коду.
* Економія пам'яті (порівняно зі звичайними класами або словниками).
* Незмінність (immutable), як і у звичайних кортежів.
"""
# %%

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p1 = Point(2, 3)
p2 = Point(x=5, y=7)

print(p1)
print(p1.x, p1.y)


print(p1._asdict())

# Створення "копії" з оновленим полем
p3 = p1._replace(x=10)
print(p3)

isinstance(p2, tuple)

# %%

"""**Задача**

Зберегти координати точок та обчислити їх відстань до початку координат.
"""

from collections import namedtuple
import math

Point = namedtuple('Point', ['x', 'y'])

points = [Point(0, 0), Point(3, 4), Point(-2, 5)]

distances = [math.hypot(p.x, p.y) for p in points]
print(distances)  # [0.0, 5.0, ~5.385]

# %%


"""
**Задача**

У нас є список співробітників. Необхідно знайти всіх розробників та обчислити їхню середню зарплату."""

from collections import namedtuple

# Створення структури даних
Employee = namedtuple('Employee', ['name', 'role', 'salary'])

# Імітація бази даних
staff = [
    Employee('Alex', 'Developer', 4000),
    Employee('Olga', 'Manager', 3500),
    Employee('Ivan', 'Developer', 4200),
    Employee('Dmytro', 'Designer', 3000),
    Employee('Sara', 'Developer', 3800)
]

developers_salaries = [e.salary for e in staff if e.role == 'Developer']

if developers_salaries:
    avg_salary = sum(developers_salaries) / len(developers_salaries)
    print(f"Кількість розробників: {len(developers_salaries)}")
    print(f"Середня зарплата: ${avg_salary:.2f}")
else:
    print("Розробників не знайдено.")

# %%


"""**Задача**

Створіть структуру даних для товару (Назва, Категорія, Ціна, Наявність).
Створіть список із 5-6 товарів. Знайдіть всі товари, які є в наявності (`in_stock=True`) і коштують менше 500 грн.

"""

from collections import namedtuple

Product = namedtuple('Product', ['name', 'category', 'price', 'in_stock'])

catalog = [
    Product('Mouse', 'Electronics', 450, True),
    Product('Keyboard', 'Electronics', 1200, True),
    Product('Monitor', 'Electronics', 5000, False),
    Product('USB Cable', 'Accessories', 150, True),
    Product('Webcam', 'Electronics', 800, True),
    Product('Mousepad', 'Accessories', 200, False)
]

affordable_items = [
    p for p in catalog
    if p.in_stock and p.price < 500
]

print("Доступні товари до 500 грн:")
for item in affordable_items:
    print(f"- {item.name} ({item.price} грн)")

# %%

"""# Лічильник (`Counter`)

`Counter` — це спеціалізований словник для підрахунку хешованих об'єктів. Елементи зберігаються як ключі словника, а їхня кількість — як значення.

**Ключові методи:**
* `most_common(n)` — повертає `n` найпопулярніших елементів.
* `update()` — додає нові дані до існуючого лічильника.


"""

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)

import collections

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts)

print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))


# %%


"""**Задача**

Проаналізувати рядок замовлень (товарів), розділених комою, та вивести топ-3 найпопулярніших товари.
"""

from collections import Counter

raw_orders = "apple,banana,apple,orange,banana,apple,grape,banana,kiwi,orange,apple"
order_list = raw_orders.split(',')

inventory = Counter(order_list)

print(f"Повний підрахунок: {inventory}")

print("\n--- ТОП-3 Товарів ---")
for item, count in inventory.most_common(2):
    print(f"Товар: {item} | Продано: {count}")


# %%


"""Приклад: підрахунок частоти слів"""

from collections import Counter

text = "python is great and python is easy to learn"
words = text.split()

word_counts = Counter(words)
print(word_counts)

print(word_counts.most_common(3))

# %%


"""Приклад: лічильник символів"""

from collections import Counter

s = "abracadabra"
char_counts = Counter(s)

print(char_counts['a'])
print(char_counts)

# %%


"""**Задача**

Напишіть програму, яка приймає довгий рядок тексту, очищує його від знаків пунктуації, розбиває на слова (ігноруючи регістр) і виводить 5 найпопулярніших слів із зазначенням їх кількості.

"""

from collections import Counter
import string

text = """
Python is great. Python is easy to learn. The collections module in Python is powerful.
Python code is clean. Learning Python is fun. Code, code, code!
"""

# 1. Очистка та нормалізація
translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator).lower()
words = clean_text.split()

# 2. Підрахунок
word_counts = Counter(words)

# 3. Вивід топ-5
print("ТОП-5 слів:")
for word, count in word_counts.most_common(5):
    print(f"'{word}': {count}")


# %%


"""# Словник зі значенням за замовчуванням (`defaultdict`)

Звичайний словник (`dict`) видає помилку `KeyError`, якщо ви намагаєтесь звернутися до неіснуючого ключа.
`defaultdict` дозволяє задати функцію (наприклад, `list`, `int`, `set`), яка автоматично створює порожнє значення при зверненні до нового ключа.


"""

tmp_dict = dict()

tmp_dict

tmp_dict['first'] = [1,3,4]

tmp_dict

from collections import defaultdict

students_data = [
    ('Anna', 'A'), ('Bob', 'B'), ('Clara', 'A'),
    ('Dave', 'C'), ('Eve', 'B'), ('Frank', 'A')
]

grades_book = defaultdict(list)

for name, grade in students_data:
    grades_book[grade].append(name)

import json
print(json.dumps(grades_book, indent=2))

# %%


"""**Задача**

Згрупувати числа (парні та непарні)

"""

from collections import defaultdict

numbers = [1, 2, 3, 4, 5, 6]

print("--- 1. Звичайний dict (Поганий спосіб - Помилка) ---")
d1 = {}
try:
    for n in numbers:
        key = 'even' if n % 2 == 0 else 'odd'

        d1[key].append(n)
except KeyError as e:
    print(f"Помилка: Ключ {e} не знайдено!")


print("\n--- 2. Звичайний dict (Робочий спосіб) ---")
d2 = {}
for n in numbers:
    key = 'even' if n % 2 == 0 else 'odd'

    if key not in d2:
        d2[key] = []

    d2[key].append(n)
print(f"Результат: {d2}")


print("\n--- 3. defaultdict (Ідеальний спосіб) ---")

d3 = defaultdict(list)

for n in numbers:
    key = 'even' if n % 2 == 0 else 'odd'
    d3[key].append(n)

print(f"Результат: {dict(d3)}")

# %%


"""**Задача**

Згрупувати студентів за оцінками.
Вхідні дані: список пар `(Ім'я, Оцінка)`.
Вихідні дані: словник `{Оцінка: [список імен]}`.
"""

from collections import defaultdict

students_data = [
    ('Anna', 'A'), ('Bob', 'B'), ('Clara', 'A'),
    ('Dave', 'C'), ('Eve', 'B'), ('Frank', 'A')
]


grades_book = defaultdict(list)

for name, grade in students_data:
    grades_book[grade].append(name)

import json
print(json.dumps(grades_book, indent=2))

# %%


"""**Задача**

Є список слів. Створіть словник, де ключем є перша літера слова, а значенням — список усіх слів, що починаються на цю літеру.


"""

from collections import defaultdict

words = ['apple', 'banana', 'apricot', 'cherry', 'blueberry', 'avocado', 'cabbage']

dictionary = defaultdict(list)

for word in words:
    first_letter = word[0].upper()
    dictionary[first_letter].append(word)

print(dict(dictionary))

# %%


"""# Структури даних: Стек, Черга та Дек (Deque)

* **Стек (LIFO - Last In, First Out)**

    Останній прийшов — перший пішов. Використовується для "Undo" операцій, перевірки дужок. Реалізується через `list`.

* **Черга (FIFO - First In, First Out)**

    Перший прийшов — перший пішов.

* **Deque (Double-ended queue)**

    Оптимізована черга з модуля `collections`. Дозволяє додавати/видаляти елементи з обох кінців за час **O(1)**. Звичайний список робить це повільно (O(n)) для початку списку.

Реалізація стеку через список
"""

# Створення стеку
def create_stack():
    return []

# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0

# Додавання елементу
def push(stack, item):
    stack.append(item)

# Вилучення елементу
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")

stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')

print(peek(stack))

print(pop(stack))

from collections import deque

# Стек
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.pop())
print(stack.pop())

# Черга
queue = deque()
queue.append("task1")
queue.append("task2")
queue.append("task3")
print(queue.popleft())
print(queue.popleft())

# Двостороння черга
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)

# %%

"""**Задача**

Емуляція черги друку (FIFO) через `deque`.

"""

from collections import deque

print("--- 1. Черга друку ---")
printer_queue = deque()

printer_queue.append("Document1.pdf")
printer_queue.append("Photo.jpg")
printer_queue.append("Report.docx")

while printer_queue:
    current_job = printer_queue.popleft()
    print(f"🖨️ Друкується: {current_job}")

# %%

"""**Задача**

Валідація правильності дужок через Стек.
"""

print("\n--- 2. Валідація дужок ---")

def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in pairs.values():  # Якщо відкриваюча дужка (, [, {
            stack.append(char)
        elif char in pairs.keys():  # Якщо закриваюча ), ], }
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

test_str = "{[()]}"
print(f"Вираз '{test_str}' коректний? -> {is_balanced(test_str)}")

test_str_bad = "{[(])}"
print(f"Вираз '{test_str_bad}' коректний? -> {is_balanced(test_str_bad)}")

# %%

"""**Задача**

Реалізуйте простий механізм збереження історії змін тексту. Є команди "Write" (додати текст) та "Undo" (видалити останній доданий фрагмент).


"""

text_buffer = ""
history_stack = []

def write(text):
    global text_buffer
    history_stack.append(text_buffer)
    text_buffer += text
    print(f"Write: '{text}' -> Поточний текст: '{text_buffer}'")

def undo():
    global text_buffer
    if history_stack:
        text_buffer = history_stack.pop()
        print(f"Undo -> Поточний текст: '{text_buffer}'")
    else:
        print("Нічого скасовувати")

write("Hello")
write(" World")
write("!!!")

undo()
undo()
undo()
undo()

# %%

"""# ChainMap (Ланцюг відображень)

`ChainMap` об'єднує кілька словників в один логічний блок. Це дуже корисно для керування налаштуваннями з пріоритетами (наприклад: *аргументи командного рядка* > *змінні середовища* > *значення за замовчуванням*).


Пошук ключа відбувається послідовно в кожному словнику ланцюга. Запис (зміна значення) завжди відбувається в **першому** словнику.
"""

from collections import ChainMap

defaults = {'theme': 'Light', 'user': 'Guest', 'debug': False}
env_vars = {'user': 'Admin', 'debug': True}  # Змінні середовища
cli_args = {'theme': 'Dark'}                 # Аргументи запуску (найвищий пріоритет)

# Створення ланцюга (порядок важливий: від найвищого пріоритету до найнижчого)
config = ChainMap(cli_args, env_vars, defaults)
# config = ChainMap(defaults, cli_args, env_vars)

print(f"Активна тема: {config['theme']}")
print(f"Користувач:   {config['user']}")
print(f"Налагодження: {config['debug']}")

config['new_param'] = 123
print(f"\nЗмінений cli_args: {cli_args}")
print(f"Змінений defaults: {defaults}")

# %%

"""# OrderedDict (Впорядкований словник)

Хоча звичайні словники (`dict`) у Python 3.7+ також зберігають порядок вставки, `OrderedDict` має унікальні можливості:
1.  **`move_to_end(key, last=True)`**. Ефективно переміщує існуючий ключ у кінець або початок словника.
2.  **Порівняння**. `OrderedDict` враховує порядок елементів при перевірці на рівність (на відміну від звичайного `dict`).

Це корисно для реалізації LRU-кешів (Last Recently Used) або коли порядок ключів критично важливий для логіки.
"""

from collections import OrderedDict

# Створення словника
d = OrderedDict.fromkeys(['a', 'b', 'c', 'd', 'e'])
print(f"Початковий вигляд: {list(d.keys())}")

# Переміщення елемента 'b' в кінець (ніби ми його щойно використали)
d.move_to_end('b')
print(f"Після move_to_end('b'): {list(d.keys())}")

# Переміщення елемента 'e' на початок
d.move_to_end('e', last=False)
print(f"Після move_to_end('e', last=False): {list(d.keys())}")

# Демонстрація різниці порівняння
d1 = OrderedDict({'a': 1, 'b': 2})
d2 = OrderedDict({'b': 2, 'a': 1})
print(f"\nOrderedDict d1 == d2? -> {d1 == d2}") # False, бо різний порядок

d3 = {'a': 1, 'b': 2}
d4 = {'b': 2, 'a': 1}
print(f"Звичайний dict d3 == d4? -> {d3 == d4}") # True, порядок ігнорується

# %%


"""# Модуль `decimal`

https://docs.python.org/uk/3/library/decimal.html

Числа з плаваючою крапкою (`float`) базуються на двійковій системі, тому `0.1 + 0.2` в Python не дорівнює точно `0.3`.
Для наукових та фінансових розрахунків це неприпустимо. Модуль `decimal` дозволяє задавати довільну точність і працювати з числами так, як це роблять люди (десяткова система).

**Важливо**

Ініціалізувати `Decimal` слід з **рядка** ('0.1'), а не з числа (0.1), інакше точність втрачається ще до створення об'єкта.

**Задача**

Розрахувати податок і загальну суму з точним округленням до копійок.
"""

from decimal import Decimal, ROUND_HALF_UP

# Демонстрація проблеми float
print(f"Float math: 0.1 + 0.2 = {0.1 + 0.2}")

# Використання Decimal
price = Decimal('19.99')
quantity = Decimal('3')
tax_rate = Decimal('0.075')  # 7.5%

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

final_total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f"\n--- Чек ---")
print(f"Підсумок: {subtotal}")
print(f"Податок (точний): {tax}")
print(f"До сплати: {final_total}")

# %%


"""# Генератори

Генератори — це функції, які використовують `yield` замість `return`. Вони не повертають всі дані одразу, а створюють ітератор, який генерує значення "на льоту" (по одному за запитом).

**Перевага**

Критична економія оперативної пам'яті (RAM) при роботі з великими даними.

**Задача**

Порівняти використання пам'яті між списком і генератором при обробці мільйона чисел.
"""

import sys

# Функція, що створює список (завантажує пам'ять)
def get_squares_list(n):
    return [i ** 2 for i in range(n)]

# Функція-генератор (ліниве обчислення)
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2

N = 1_000_000

list_obj = get_squares_list(N)
print(f"Розмір списку в пам'яті: {sys.getsizeof(list_obj) / 1024 / 1024:.2f} MB")

gen_obj = get_squares_gen(N)
print(f"Розмір генератора в пам'яті: {sys.getsizeof(gen_obj)} Bytes")

print("\nДемонстрація роботи генератора (перші 3 значення):")
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))