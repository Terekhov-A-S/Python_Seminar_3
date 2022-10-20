# Задача 22. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def sum_of_numbers(num):
    count = 0
    for i in range(len(num)):
        if i % 2 != 0:
            count += num[i]
    print(f"Сумма равна: {count}")


numbers = list(map(int, input("Задайте список чисел через пробел: ").split()))
sum_of_numbers(numbers)
