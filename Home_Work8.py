# Напишите программу, которая на вход получает число n и считает по нему сумму 1²+2²+3²+...+n².
# Ограничение: нельзя пользоваться функцией sum() и ее аналогами.

encoding = 'utf-8'
number = int(input("Введите число: "))
numbers_sum = 0
for i in range (1,number + 1):
    numbers_sum += i ** 2
print (numbers_sum)
