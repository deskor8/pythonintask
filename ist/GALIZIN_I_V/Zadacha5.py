# Задача 5. Вариант 9.
#  Напишите программу, которая бы при запуске случайным образом отображала название одной из трех стран, входящих в военно-политический блок "Антанта".

# Galizin I.V.
# 22.04.2017

import random
country=['Россия', 'Великобритания', 'Франция']
print(random.choice(country))
input("Нажмите Enter для выхода.")