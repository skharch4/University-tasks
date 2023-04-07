"""
Напишіть функцію read_last(lines, file) , яка відкриватиме певний файл file
і виводити на друк по рядкам останні рядки у кількості lines (про всяк випадок
перевіримо, що задано позитивне ціле число). Протестуйте функцію на файлі
article.txt з наступним вмістом:
Завдання №1
"""
def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print('Кількість строк потрібна бути тільки цілим позитивним')
#Тестуємо функцію.
read_last(5, 'article.txt')

