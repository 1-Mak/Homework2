import random

dimension = int(input('Введите размерность массива:'))
massive = [0.0]*dimension
for i in range(dimension):
    massive[i] = (random.randint(1,100)/10)
maximum = max(massive)
print('Входной массив:',massive)
for i in range(dimension):
    if maximum == massive[i]:
        for j in range(i+1,dimension):
            massive[j] = 0

print('Результат:',massive)