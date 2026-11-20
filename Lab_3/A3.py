print('Введите предыдущее показание счетчика:')
previous = int(input())
print('Введите текущее показание счетчика:')
current = int(input())
if current >= previous:
    used = current - previous
else:
    used = current + 10000 - previous
if used <= 300:
    money = 21
elif used <= 600:
    money = 21 + (used - 300) * 0.06
elif used <= 800:
    money = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    money = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
average = money / used
print("Предыдущее    Текущее    Использовано    К оплате    Ср. цена м^3")
print(previous, current, used, format(money, ".2f"), format(average, ".2f"), sep='          ')