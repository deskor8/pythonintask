# Задача 8. Вариант 13. 
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка.
#Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
#Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.


# Suchkov R.A. 
# 25.03.2017


import random
anag = ("жизнь", "задача", "учеба", "машина", "компьютер", "экзоскилет")
ranag = random.choice(anag)
correct = ranag
 
bad = "Не знаю"
pomos = ranag[0] + ranag[1] + ranag[2] + ranag[3]
pperem = ""
while ranag:
    position = random.randrange(len(ranag))
    pperem += ranag[position]
    ranag = ranag[:position] + ranag[(position + 1):]
 
score = 10
print("""Добро пожаловать в игру 'Анаграммы'! 
 	Надо переставить буквы так, чтобы получилось осмысленное слово.
 	Если вам нужна подсказкавведите: "Не знаю".
        Но за помощь вы получите меньше очков.
                             (Для выхода нажмите Enter, не вводя своей версии.)""")
print("Вот анаграмма: ", pperem)
ans = input("\nПопробуйте отгадать исходное слово: ")
while ans != "" and ans != correct:
    if ans != correct and not ans == bad:
        print("Вы не отгадали.")
        ans = input("\nПопробуйте отгадать исходное слово: ")
    if ans == bad:
        score -= 5
        print("\nПервые три буквы слова!", pomos)
        ans = input("Попробуйте отгадать загаданное слово: ")
    if ans == correct:
            print("Поздравляю!! Вы отгадали\n")
 
if score < 0:
     score = 0
print("Вы заработали", score, "очков!")
input("\n\nНажмите Enter для выхода")  

