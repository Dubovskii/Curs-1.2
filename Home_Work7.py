# Напишите программу, которая поможет составить план тренировок для подготовки к марафону.
# Она получает на вход число километров на планируемом марафоне, сколько пользователь планирует пробежать в первый день
# тренировок и на сколько процентов планирует увеличивать каждый день это расстояние. На выходе программа
# должна выдавать, сколько дней пользователю потребуется для того, чтобы подготовиться пробежать
# целевое количество километров.
# Ограничение: нельзя пользоваться функцией ceil() из модуля math и ее аналогами.


encoding = 'utf-8'
days = 0
marathon = float(input("Введите длину марафонской дистанции: "))
start_run = float(input("Введите количество километров для первой пробежки: "))
add_run = float(input("Введите на сколько процентов планируется увеличивать пробежку ежедневно: "))
probeg = start_run
while probeg < marathon:
    days += 1
    probeg += probeg / 100 * add_run
print (days)