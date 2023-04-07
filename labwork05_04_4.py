"""
Завдання 4
Треба створити csv-файл rows_300.csv з такими стовпчиками:
- № - номер по порядку (від 1 до 300); – секунда – потокова секунда на ПК;
– Мікросекунда – потокова мілісекунда на годиннику. На кожній ітерації циклу
штучно зупиняйте скрипт на 0,01 секунди.
(Використати import csv import datetime import time)
"""
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунди ', 'Мікросекунди'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)