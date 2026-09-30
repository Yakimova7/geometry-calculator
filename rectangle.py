python
class Rectangle:
 def __init__(self, width: float, height: float):
 if width <= 0 or height <= 0:
 raise ValueError("Стороны должны быть положительными")
 self.width = width
 self.height = height
 def area(self) -> float:
 return self.width * self.height
