#Здача 7. Вариант 14
#Разработайте систему начисления очков для задачи 6, в соответвии с которой игрок получал бы больгее кол-во баллов за меньшее кол-во попыток.

#Kartinceva A.U.
#19.04.17

import random
talisman = random.choice(["Леопард","Зайка","Белый Мишка"])
h = 3
n = 4
print("Программа случайным образом загадала одного из трех официальных талисманов Олимпийских игр 2014!")
print("Отгадайте за минимальное кол-во попыток!")
print("\nМаксимальное кол-во очков: 12")
while h>0:
	ask = input("Ваш ответ: ")
	if ask == talisman:
		print ("Отлично!")
		break
	else:
		print ("Простите, но не правильно!")
		h = h - 1
print ("Кол-во очков = ", h * n)
print ("Спасибо за то, что сыграли в игру!")
input ("\nPress Enter to exit")