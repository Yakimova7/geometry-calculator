import math

# Начальная сумма
total_sum = 0

# Цикл от 1 до 50 включительно
for n in range(1, 51):
    # Считаем числитель: (2n + 1)
    numerator = 2 * n + 1
    
    # Считаем знаменатель: n! (факториал)
    # math.factorial(n) вычисляет факториал
    denominator = math.factorial(n)
    
    # Считаем степень: (sin n)^(n+1)
    # math.sin(n) - синус числа n (в радианах)
    # ** (n+1) - возведение в степень n+1
    power_part = math.sin(n) ** (n + 1)
    
    # Считаем текущий член ряда
    term = (numerator / denominator) * power_part
    
    # Добавляем к общей сумме
    total_sum += term

# Выводим результат
print(f"Сумма ряда S = {total_sum}")