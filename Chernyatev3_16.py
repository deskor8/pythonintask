﻿# Задача 3, Вариант 16
# Напишите программу, которая выводит имя "Мария Луиза Полякова — Байдарова", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Чернятьев И.К.
# 18.04.17

name = "Мария Луиза Полякова — Байдарова"
print("Сегодня мы познакомимся с - " + name)
name2 = input("Какой псевдоним у этого человека?? Ваш ответ: ")
print("Все верно: " + name + " - " + name2)
input("Нажмите Enter для выхода")