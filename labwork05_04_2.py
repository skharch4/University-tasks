"""Виберіть будь-яку папку на своєму комп'ютері з вкладеними каталогами.
Виведіть на друк у термінал її вміст, як і всі підкаталоги за допомогою функції
print_docs(directory) .
(Використати модуль OS)
"""
import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} містить:') #Друкуємо "папка", її адрес, те що вона містить
    print(f'Директорії: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файли: {", ".join([file for file in catalog[2]])}') #вказуємо на зміст директорії

#Виводимо нашу функцію та вказуємо директорію
print_docs('C:/Users/skharch4/labs')