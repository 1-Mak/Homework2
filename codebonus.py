import random

dimension = int(input('Введите размерность массива:'))
delta = float(input('Введите DELTA:'))
massive = [0]*dimension
count = 0
for i in range(dimension):
    massive[i] = (random.randint(1,10))
minimal = min(massive)
for i in range(dimension):
    if massive[i] - delta == minimal:
        count +=1
print(count)