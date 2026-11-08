# нахождение среднего геометрического и среднего арифметического

x = float(input('Введите действительное число'))
y = float(input('Введите действительное число'))
if x * y >= 0:
    srgeom = (x*y)**0.5
    print(srgeom)
else:
    srarifm = (x+y) / 2
    print(srarifm)
