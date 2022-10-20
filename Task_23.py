# Задача 23. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def product_of_pairs_numbers(num):
    count = len(num) // 2 + 1 if len(num) % 2 != 0 else len(num) // 2
    pairs_numbers = [num[i] * num[len(num) - i - 1] for i in range(count)]
    print(pairs_numbers)


numbers = list(map(int, input("Для подсчета произведения чисел, введите их через пробел: ").split()))
product_of_pairs_numbers(numbers)
