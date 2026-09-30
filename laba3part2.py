import math

# Задаем границы и шаг
a = 0.1
b = 0.7
step = 0.1  # Шаг изменения x (если в задании другой, поменяйте здесь)

# Переменная x будет меняться от a до b
x = a
while x <= b + 1e-9:  # 1e-9 добавлено, чтобы избежать ошибок округления
    # Считаем первую часть: sin^3(x^2) / cos^2(x^3)
    # В Python sin^3(x^2) записывается как math.sin(x**2)**3
    numerator = math.sin(x**2)**3
    denominator = math.cos(x**3)**2
    
    # Проверяем, не равен ли знаменатель нулю, чтобы избежать деления на ноль
    if denominator == 0:
        part1 = float('inf')  # бесконечность
    else:
        part1 = numerator / denominator

    # Считаем вторую часть: sqrt((3 + x^2) / (1 - 2x^3))
    # math.sqrt() - квадратный корень
    inner_expr = (3 + x**2) / (1 - 2 * x**3)
    
    # Проверяем, не отрицательное ли подкоренное выражение
    if inner_expr < 0:
        part2 = float('nan')  # не число (ошибка)
    else:
        part2 = math.sqrt(inner_expr)

    # Итоговый y
    y = part1 + part2

    # Выводим результат, округляя до 4 знаков
    print(f"x = {x:.1f}, y = {y:.4f}")
    
    # Увеличиваем x на шаг
    x += step