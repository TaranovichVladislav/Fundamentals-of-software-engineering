import sys
bytes_count = 1921000
megabytes = bytes_count / (1024 * 1024)
print(f"Число занимает {megabytes:.3f} Мегабайт (МБ)")
print("Пожалуйста, подождите, вычисляем 3**9090001...")
big_number = 3 ** 9090001
size_in_bytes = sys.getsizeof(big_number)
print(f"Размер числа (в байтах) через getsizeof: {size_in_bytes} байт")
size_in_mb = size_in_bytes / (1024 * 1024)
print(f"Размер числа (в МБ) через getsizeof: {size_in_mb:.3f} МБ")