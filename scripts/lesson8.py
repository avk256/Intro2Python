
"""
## 1. Імпорт пакетів та модулів

У Python **import** дозволяє підключати зовнішній код (стандартну бібліотеку, сторонні пакети, власні модулі). Це дає змогу:

- розбивати великий проєкт на логічні частини;
- повторно використовувати код;
- підключати готові бібліотеки.

Основні форми імпорту:

- `import math` — імпорт цілого модуля, використання як `math.sin`, `math.pi`;
- `import math as m` — те саме, але з псевдонімом `m`;
- `from math import sqrt` — імпорт конкретної функції `sqrt` у поточний простір імен;
- `from math import sin, cos` — імпорт кількох конкретних імен;
- `from math import *` — імпорт усіх “публічних” імен (у реальних проєктах краще уникати, бо це забруднює простір імен та ускладнює читання).

Імпорт — базовий механізм організації коду в Python.
"""
# %%
import math
print("pi =", math.pi)
print("cos(pi) =", math.cos(math.pi))

# Імпорт з псевдонімом
import math as m
print("sin(pi/2) =", m.sin(m.pi / 2))

# Імпорт конкретної функції
from math import sqrt
print("sqrt(16) =", sqrt(16))

# Комбінований імпорт
from math import sin, cos
print("sin(0) =", sin(0), "cos(0) =", cos(0))

# %% 

"""
## 2. Поняття модуля в Python. Створення модулів

**Модуль** у Python — це звичайний файл з розширенням `.py`, який містить:

- змінні;
- функції;
- класи;
- виконуваний код (за потреби).

Наприклад, файл `my_module.py` з визначеннями функцій та змінних уже є модулем.

Щоб скористатися модулем в іншому файлі, достатньо:

1. створити файл `my_module.py` з кодом;
2. у іншому файлі написати `import my_module`;
3. звертатися до вмісту як `my_module.імʼя`.

"""

import os
import sys

print(os.getcwd())

print(os.path.dirname(__file__))

# Додати корінь проєкту в sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

print(PROJECT_ROOT)

sys.path.append(PROJECT_ROOT)

from my_package import mymodule



print(mymodule.greet("Олексій"))
print("2 + 3 =", mymodule.add(2, 3))
print("PI =", mymodule.PI)

# Імпорт окремих імен
from my_package.mymodule import greet, PI
print(greet("Python"))
print("PI from direct import:", PI)


# %%

"""
## 3. Як Python шукає модулі?

Коли інтерпретатор бачить інструкцію `import імʼя_модуля`, він шукає модуль у такій послідовності:

1. **Вбудовані модулі**  
   Перевіряється, чи ім’я відповідає вбудованому модулю стандартної бібліотеки (наприклад, `sys`, `math`).

2. **Поточна директорія**  
   Шукається файл `імʼя_модуля.py` або директорія `імʼя_модуля` (пакет) у поточній директорії, з якої був запущений скрипт.

3. **Шляхи з `sys.path`**  
   Якщо модуль не знайдено в поточній директорії, пошук продовжується по списку шляхів `sys.path`. До нього входять:
   - директорії стандартної бібліотеки;
   - директорії з установленими сторонніми пакетами (site-packages);
   - додаткові шляхи, додані вручну.

Якщо модуль не знайдений ніде, виникає помилка `ModuleNotFoundError`.

Отже, **місце файлу** і вміст `sys.path` визначають, чи можна імпортувати модуль.

"""

# 3. де Python шукає модулі

import sys

print("Шляхи пошуку модулів (sys.path):")
for p in sys.path:
    print(" ", p)

# %%
"""
## 4. Функція `dir()` та службова змінна `__name__`

### 4.1. `dir()`

`dir()` — вбудована функція для дослідження простору імен:

- `dir()` без аргументів повертає список імен, визначених у поточному просторі (змінні, функції, модулі тощо);
- `dir(obj)` повертає список атрибутів/імен, визначених в об’єкті `obj` (модулі, класи, екземпляри).

Це корисно для швидкого ознайомлення з вмістом модуля або об’єкта в інтерактивному середовищі.

### 4.2. `__name__`

Кожен модуль має службову змінну `__name__`:

- якщо файл **запускається напряму** як скрипт, тоді `__name__ == "__main__"`;
- якщо файл **імпортується як модуль**, тоді `__name__ == "імʼя_модуля"`.

Це дозволяє писати:

```python
if __name__ == "__main__":
    main()
"""


# 4.1. Використання dir()

import math

print("Імена, визначені в модулі math:")
print(dir(math)[:20], "...")  # виведемо перші 20 для стислості

print("\nІмена в поточному просторі імен:")
print(dir()[:20], "...")

from my_package import name_demo

# %%

"""
## 5. Модуль `sys`. Обробка аргументів командного рядка

**Модуль `sys`** надає доступ до змінних і функцій, повʼязаних з інтерпретатором Python.

Один із ключових елементів — список `sys.argv`:

- `sys.argv[0]` — імʼя запущеного скрипта;
- `sys.argv[1:]` — аргументи, передані скрипту з командного рядка.

"""

import sys

def main():
    print("Імʼя скрипта:", sys.argv[0])
    print("Аргументи:", sys.argv[1:])

    if len(sys.argv) >= 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        print(f"{a} + {b} = {a + b}")
    else:
        print("Передайте два числа як аргументи.")

if __name__ == "__main__":
    main()


#%%

"""
Створення та використання модулів пакету 

https://github.com/ahmedfgad/GeneticAlgorithmPython/tree/master

"""


import my_package

from my_package import math_utils, string_utils

print("2 + 3 =", math_utils.add(2, 3))
print("2 * 3 =", math_utils.mul(2, 3))
print(string_utils.shout("hello world"))

#%% 

"""
## 7. Пакетний менеджер `pip`

https://pypi.org/

https://docs.conda.io/en/latest/

**`pip`** — стандартний менеджер пакетів у Python. Він дозволяє:

- встановлювати сторонні бібліотеки з PyPI;
- оновлювати їх;
- видаляти;
- фіксувати список залежностей у файлі `requirements.txt`.

Типові команди (у терміналі):

- `pip install requests` — встановити пакет;
- `pip install "numpy==1.26.0"` — встановити конкретну версію;
- `pip install -U requests` — оновити пакет;
- `pip uninstall requests` — видалити пакет;
- `pip list` — показати встановлені пакети;
- `pip freeze > requirements.txt` — зберегти поточний список пакетів у файл.


"""

# 7.1. Встановимо пакет requests (у Colab він може бути вже встановлений)

import requests
response = requests.get("https://google.com")
print("Статус:", response.status_code)
print("Частина тіла відповіді:", response.text[:80], "...")

#%%

"""
## 8. Керування середовищами

env
-----------------------------------------
### 1. Створення віртуального середовища

У корені проєкту:

python -m venv .venv

Тут `.venv` — папка з вашим середовищем (можна назвати інакше).

---

### 2. Активація

### Linux / macOS (bash/zsh)

source .venv/bin/activate

У консолі з’явиться префікс типу `(.venv)` — це означає, що середовище активне.

### Windows PowerShell

.\.venv\Scripts\Activate.ps1

---

### 3. Інсталяція пакетів всередині env

Після активації:

pip install numpy pandas requests

Список установлених пакетів:

pip list

Зберегти залежності в файл:

pip freeze > requirements.txt

Встановити залежності з файлу:

pip install -r requirements.txt

---

### 4. Деактивація

Коли закінчили роботу:

deactivate

Префікс `(.venv)` зникне

conda
--------------------------------------------------

### 1. Створення середовища

### Без вказання версії Python

conda create -n myenv

### З конкретною версією Python

conda create -n myenv python=3.11

`myenv` — назва середовища (довільна).

---

### 2. Активація / деактивація

### Активувати

conda activate myenv

У рядку терміналу з’явиться префікс `(myenv)` — середовище активне.

### Деактивувати

conda deactivate

Префікс зникне — повернення до базового середовища (`base`) або системного Python.

---

### 3. Інсталяція пакетів

### Через conda (краще, коли пакет є в репозиторіях conda)

conda install numpy pandas

Можна вказати канал (наприклад, `conda-forge`):

conda install -c conda-forge jupyterlab

### Через pip (якщо пакета немає в conda)

(Уже всередині активного середовища!)

pip install seaborn

---

## 4. Список середовищ

conda env list
# або
conda info --envs

---

## 5. Видалення середовища

conda remove -n myenv --all

---

### 6. Експорт / імпорт середовища (для проєктів)

### Експортувати у `environment.yml`

conda env export -n myenv > environment.yml

### Створити середовище з `environment.yml`

conda env create -f environment.yml

"""
