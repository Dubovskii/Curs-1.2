# Напишите программу, которая на вход получает число n и считает по нему сумму сумму 1! + 2! + 3! + ... + n!
# Ограничение: нельзя пользоваться готовой функцией factorial() из модуля math, функцией sum() и их аналогами.

number = int(input("Введите число: "))
numbers_sum = 0
factorial= 1
for i in range (1,number + 1):
    for n in range (1, i + 1):
        factorial *= n
    numbers_sum += factorial
    factorial = 1
print (numbers_sum)
