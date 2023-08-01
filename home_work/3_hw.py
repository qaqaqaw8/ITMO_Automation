def ht1(a, b):
    return max(a,b)
print(ht1(10,3))

def ht2(c,d):
    if c-d == 135 or d-c == 135:
        print('Yes')
    else:
        print('no')
ht2(15,150)

def ht3(t):
    if t>=1 and t<3 or t == 12:
        print("зима")
    elif t>=3 and t<6:
        print('весна')
    elif t>=6 and t<9:
        print('лето')
    elif t>=9 and t<12:
        print('осень')
    else:
        print('Введите значение от 1 до 12')
ht3(10)