# Задача 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.


decimal_number = int(input("Введите десятичное число: "))
binary_number: str = ""
while decimal_number != 0:
    binary_number: str = str(decimal_number % 2) + binary_number
    decimal_number //= 2
print(binary_number)
