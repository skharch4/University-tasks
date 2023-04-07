"""
Завдання 3
Документ article.txt містить наступний текст:
Вечоріло .
Гули мухи.
Світив ліхтарик.
Кипіла вода в чайнику.
Венера спалахнула на небі.
Дерева шуміли.
Хмари розійшлися.
Листя зеленіло.
Потрібно реалізувати функцію longest_words(file) , яка виводить слово, що
має максимальну довжину (або список слів якщо таких декілька).

"""


def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        return sought_words


print(longest_words('article.txt'))