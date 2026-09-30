import math

# Задаем значение x
x = math.pi / 8

# Считаем первую часть: 3 * |sin(x)| / |cos(3x)|
# abs() - модуль числа
part1 = (3 * abs(math.sin(x))) / abs(math.cos(3 * x))

# Считаем вторую часть: arccos(2x^2) / arcsin(3x^3)
# math.acos() - арккосинус, math.asin() - арксинус
part2 = math.acos(2 * x**2) / math.asin(3 * x**3)

# Считаем общий результат
y = part1 + part2

print(f"При x = π/8")
print(f"y = {y}")