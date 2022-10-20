# Задача 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci_numbers(i):
    if i in [1, 2]:
        return 1
    else:
        return fibonacci_numbers(i - 1) + fibonacci_numbers(i - 2)


def negafibonacci_numbers(i):
    if i == 1:
        return 1
    elif i == 2:
        return -1
    else:
        a, b = 1, -1
        for j in range(2, i):
            a, b = b, a - b
        return b


numbers = [0]
enter_number = int(input('Введите число: '))
for k in range(1, enter_number + 1):
    numbers.append(fibonacci_numbers(k))
    numbers.insert(0, negafibonacci_numbers(k))
print(numbers)
