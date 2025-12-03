print("Всередині name_demo.py")
print("__name__ =", __name__)

if __name__ == "__main__":
    print("Цей файл запущений безпосередньо як скрипт")
else:
    print("Цей файл імпортовано як модуль")
