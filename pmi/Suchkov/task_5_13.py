# Задача 5. Вариант 13. 
# Напишите программу, которая бы при запуске случайным образом отображала
#имя одного из двенадцати апостолов.


# Suchkov R.A. 
# 28.02.2017


import  random
ap = ['Андрей', 'Петр',  'Иоанн',  'Иаков Зеведеев', 'Филлип', 'Варфоломей', 'Матфей', 'Фома', 'Иаков Алфеев', 'Иуда Фаддей', 'Симон Кананит', 'Иуда Искариот']
print ('Один из 12 апостолов ' + random.choice(ap))
input ()
