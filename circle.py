python
import math
class Circle:
 def __init__(self, radius: float):
 if radius <= 0:
 raise ValueError("Радиус должен быть положительным")
 self.radius = radius
 def area(self) -> float:
 return math.pi * (self.radius ** 2)
