# -*- coding: utf-8 -*-

print(bin(255))          
print(hex(255))          
print(format(255, 'b'))  
print(format(255, '08b'))# 
print(format(255, 'x'))  # 
print(format(255, 'X'))  # 

"""##Двійкова / шістнадцяткова → десяткова"""

print(int('11111111', 2))    
print(int('ff', 16))         
print(int('0b11111111', 0))  
print(int('0xff', 0))        

"""#Змінні: правила іменування (та створення)"""

user_name = "Oleksii"
age = 39
_mean_value = 3.14
pi = 3.14159


import keyword
print("Ключові слова:", keyword.kwlist)

x = 10
y = x + 5

# del x

print(x)
print(y)


data_none = None
data_bool = True
data_int = 123
data_float = 1.5
data_complex = 3+4j
data_str = "Привіт"
data_bytes = b"\x41\x42"
data_list = [1,2]
data_tuple = (1,2)
data_dict = {"a":1}
data_set = {1,2,3}

print(f"{data_int} -> {type(data_int)}")

print("a", "b", 123)                      # a b 123
print("root", "home", "user", sep="/")    # root/home/user

print(round(2.5), round(3.5))              # 2 4 (0.5 → до найближчого парного)
print(round(1234, -2))                     # 1200 (округлення десятків/сотень)
print(round(1.23456, 3))                   # 1.235

print(min(3, 1, 7))
print(max(3, 1, 7))

print(str(3.14))
print(str(True))

name = input("Введіть ім'я: ")
age = int(input("Вік: "))                  # каст до int вручну
print(f"{name=}, {age=}")

print(bool(0), bool(0.0), bool(""), bool([]), bool(None))
print(bool(1), bool("x"), bool([0]))

x = 10
print(dir(x))

"""#Форматований вивід через f-рядки"""

name = "Ada"
score = 93.4567
n = 255

print(f"Вітаю, {name}!")
print(f"Округлення до 2 знаків: {score:.2f}")
print(f"Шістнадцяткове: {n:#x}  Бінарне: {n:08b}")

"""#Розміри типів"""

import sys
small = 10
big = 10**100
print(sys.getsizeof(small), "байт для small int")
print(sys.getsizeof(big),   "байт для big int")

f = 3.14
z = 1+2j
print(sys.getsizeof(f), "байт для float")
print(sys.getsizeof(z), "байт для complex")

"""#Як визначити тип змінної"""

x = 2.3
print(type(x))                     # <class 'list'>
print(isinstance(x, (int, float)))  # True, якщо x list або tuple

id(x)

"""#Строки в ASCII"""

s = "Hello, world!"
b = s.encode('ascii')
print(list(b))
print(b.hex())

import this

import antigravity