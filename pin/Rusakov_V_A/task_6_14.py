# Задача 6. Вариант 14.

#Создайте игру, в которой компьютер загадывает имя одного из трех официальных талисманов зимних Олимпийских игр 2014 года в Сочи, а игрок должен его угадать.


# Русаков В.А.
# 14.04.2017

import random

print("Программа случайным образом загадывает название одного из 3-х  талисманов зимних Олимпийских игр 2014 года в Сочи, а игрок должен его угадать.")

talisman_numbers = random.randint(1,3)

if talisman_numbers == 1 :
    talisman = 'Леопард'
elif talisman_numbers == 2 :
    talisman = 'Мишка'
elif talisman_numbers == 3 :
    talisman = 'Зайка'

answer = input('\nНазовите одного из талисманов сочи 2014: ')

if answer == talisman :
    print('\nВы угадали!')
else :
    print('\nВы не угадали!!!')
    print('Правильный ответ: ', talisman)

input("\n\nНажмите Enter для выхода.")
