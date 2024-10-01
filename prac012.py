def chislo(number):
    if not isinstance(number, int):
        raise ValueError("Ошибка: входные данные должны быть целым числом.")
    if number % 2 == 0:
        return "четное"
    else:
        return "нечетное"
print(chislo(4))
print(chislo(-7))
print(chislo(0))
print(chislo(15))
print(chislo(10))
print(chislo(-2))

