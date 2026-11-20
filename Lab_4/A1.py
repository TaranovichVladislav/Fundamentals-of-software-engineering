
import random
import time
n = int(input("Введите количество примеров: "))
correct = 0
total_time = 0
for i in range(n):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    print("Вопрос", i + 1, "/", n)
    start_time = time.time()
    while True:
        try:
            answer = int(input(str(a) + " * " + str(b) + " = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    time_spent = time.time() - start_time
    total_time = total_time + time_spent
    if answer == a * b:
        print("Верно!")
        correct = correct + 1
    else:
        print("Неверно! Правильно:", a * b)
    print("Время:", round(time_spent, 1), "сек")
average_time = total_time / n
percent = correct / n * 100
print("================================")
print("СТАТИСТИКА:")
print("Общее время:", round(total_time, 1), "секунд")
print("Среднее время:", round(average_time, 1), "сек")
print("Правильных ответов:", correct, "/", n)
print("Процент правильных:", round(percent, 1), "%")