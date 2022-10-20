# Задача 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

numbers = list(map(float, input("Задайте список вещественных чисел через пробел: ").split()))
fractional_part = [round(i % 1, 2) for i in numbers if i % 1 != 0]
print(max(fractional_part) - min(fractional_part))
