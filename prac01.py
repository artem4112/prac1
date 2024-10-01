def dlina(a, b, c, d):
    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "Ошибка: стороны должны быть положительными"
    if (a + b + c >= d) or (a + b + d >= c) or (a + c + d >= b) or (b + c + d >= a):
        return "Четырёхугольник вогнутый"
    return "Четырёхугольник выпуклый"
print(dlina(3, 4, 5, 6))
print(dlina(1, 2, 3, 7))
print(dlina(0, 2, 3, 4))
print(dlina(-1, 2, 3, 4))
print(dlina(1, 'a', 3, 4))
