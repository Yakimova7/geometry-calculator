python
from circle import Circle
from rectangle import Rectangle
def main():
 print("Выберите фигуру:")
 print("1. Круг")
 print("2. Прямоугольник")

 choice = input("Введите номер: ")
 if choice == "1":
 r = float(input("Введите радиус: "))
 shape = Circle(r)
 print(f"Площадь круга: {shape.area():.2f}")
 elif choice == "2":
 w = float(input("Введите ширину: "))
 h = float(input("Введите высоту: "))
 shape = Rectangle(w, h)
 print(f"Площадь прямоугольника: {shape.area():.2f}")
 else:
 print("Неверный выбор")
if __name__ == "__main__":
 main()
