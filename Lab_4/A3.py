packets = input("Введите последовательность из 0 и 1: ")
while len(packets) < 5 or not all(char in '01' for char in packets):
    print("Ошибка! Введите минимум 5 символов, используя только 0 и 1.")
    packets = input("Введите последовательность: ")
total = len(packets)
lost = packets.count('0')
current = 0
maximum = 0
for packet in packets:
    if packet == '0':
        current = current + 1
        if current > maximum:
            maximum = current
    else:
        current = 0
percent = lost / total * 100
if percent <= 1:
    quality = "Отличное качество"
elif percent <= 5:
    quality = "Хорошее качество"
elif percent <= 10:
    quality = "Удовлетворительное качество"
elif percent <= 20:
    quality = "Плохое качество"
else:
    quality = "Критическое состояние сети"
print("Общее количество пакетов:", total)
print("Количество потерянных пакетов:", lost)
print("Длина самой длинной последовательности потерь:", maximum)
print("Процент потерь:", round(percent, 1), "%")
print("Качество связи:", quality)