# Параметры сварки
print('Меню выбора способа сварки: ')
print('1 - ручная дуговая (k = 1.0)')
print('2 - MIG/MAG (k = 1.15)')
print('3 - TIG (k = 0.85)')

while True:
    a = input("Выберите способ сварки - (1, 2 или 3):")

    if a == '1':
        k = 1.0
        U = 25
        m = 'ручная дуговая'
        continue
    elif a == '2':
        k = 1.15
        U = 25
        m = 'MIG/MAG'
        break
    elif a == '3':
        k = 0.85
        U = 20
        m = 'TIG'
        break
    else:
        print("Неверно выбран способ сварки")
while True:
    S = input("Введите толщину металла, мм (0.5..20): ")
    Ss = S.replace('.','')
    if Ss.isdigit():
        S = float(Ss)
        if 0.5 <= S <= 20:
            break
        else:
            print('Ошибка. Введите число ')
while True:
    V = input("Введите скорость сварки, м/ч (5..80): ")
    Vv = V.replace('.','')
    if Vv.isdigit():
        V = float(Vv)
        if 5 <= V <= 80:
            break
        else:
            print('Ошибка. Введите число ')
while True:
    I = input("Введите сварочный ток, А (20..400): ")
    Ii = I.replace('.','')
    if Ii.isdigit():
        I = float(Ii)
        if 20 <= I <= 400:
            break
        else:
            print('Ошибка. Введите число ')

d_e = 0.036 * (I**0.5)
n = 0.8
P = k * I * U * (n/V)
an = 10
V_napl = k * I * (an/V)

if S < 2:
    tolshina = 'тонкий металл'
elif S <= 8:
    tolshina = 'средний'
else:
    tolshina = 'толстый'

print('\n--- Резултаты расчета ---')
print(f'Способ сварки: {m}')
print(f'Диаметр электрода (d_э): {d_e:.2f} мм')
print(f'Погонная энергия (П): {P:.2f}')
print(f'Производительность (V_напл): {V_napl:.2f} г/ч')
print(f'Класс толщины: {tolshina}')
