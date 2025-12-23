# Geometric lib

## Общее описание решения
Библиотека Geometric Lib предоставляет функции для вычисления площадей и периметров основных геометрических фигур.  
Библиотека написана на Python и включает модули для работы с кругом, квадратом, прямоугольником и треугольником.
## Описание функций

### Модуль circle.py
#### area(r)
Параметры: r (float) - радиус круга
Возвращает: float - площадь круга
Пример:
circle_area = circle.area(5)
print(circle_area)  # Вывод: 78.53981633974483
#### perimeter(r)
Параметры: r (float) - радиус круга
Возвращает: float - длина окружности
Пример:
circle_perimeter = circle.perimeter(5)
print(circle_perimeter)  # Вывод: 31.41592653589793
### Модуль square.py
#### area(a)
Параметры: a (float) - длина стороны квадрата
Возвращает: float - площадь квадрата
Пример:
square_area = square.area(4)
print(square_area)  # Вывод: 16
#### perimeter(a)
Параметры: a (float) - длина стороны квадрата
Возвращает: float - периметр квадрата
Пример:
square_perimeter = square.perimeter(4)
print(square_perimeter)  # Вывод: 16
### Модуль rectangle.py
#### area(a, b)
Вычисляет площадь прямоугольника.

Параметры:
    a (float) - длина первой стороны
    b (float) - длина второй стороны
Возвращает: float - площадь прямоугольника
Пример:
rect_area = rectangle.area(3, 4)
print(rect_area)  # Вывод: 12
#### perimeter(a, b)
Параметры:
    a (float) - длина первой стороны
    b (float) - длина второй стороны
Возвращает: float - периметр прямоугольника
Пример:
rect_perimeter = rectangle.perimeter(3, 4)
print(rect_perimeter)  # Вывод: 14
### МОдуль triangle.py
#### area(a, h)
Параметры:
    a (float) - длина основания
    h (float) - высота треугольника
Возвращает: float - площадь треугольника
Пример:
triangle_area = triangle.area(6, 4)
print(triangle_area)  # Вывод: 12.0
#### perimeter(a, b, c)
Параметры:
    a (float) - длина первой стороны
    b (float) - длина второй стороны
    c (float) - длина третьей стороны
Возвращает: float - периметр треугольника
Пример:
triangle_perimeter = triangle.perimeter(3, 4, 5)
print(triangle_perimeter)  # Вывод: 12