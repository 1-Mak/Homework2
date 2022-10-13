import random

dimension = int(input('Введите размерность массивов:'))
massive = [0.0]*dimension
massive1 = [0.0]*dimension
for i in range(dimension):
    massive[i] = (random.randint(1,100)/10)
for i in range(dimension):
    massive1[i] = (random.randint(1,100)/10)
for i in range(dimension):
    for j in range(dimension):
        if massive[i] == massive1[j]:
            print(massive[i])

