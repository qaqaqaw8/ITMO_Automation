num = 0
if num>=0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

Str_1 = 'test'
str_2 = 'test1'
if  Str_1 in str_2:
    print('ДА')
else:
    print("НЕТ")


num_float = 3.4
if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print("0")
else :
    print('Отрицательное число')

permit_pint = True

if num>0 and permit_pint:
    print("num - положительное число")
elif not permit_pint:
    print("Печать запрещена")

kurs = 3
if kurs >0 and kurs <5:
    print("бакалавр")
elif kurs >4 and kurs <7:
    print("магистр")
elif kurs >6 and kurs <10:
    print("аспирант")
else:
    print("Ведите корректный год обучения")

a=33
if a in range (-100, 101):
    print("+")
else:
    print("-")
