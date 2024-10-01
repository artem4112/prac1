def find_max(arr):
    if len(arr) == 0:
        return "пустой"
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element
test_cases = [
    ([3, 5, 1, 8, 4], 8),
    ([-1, -5, -3, -4], -1),
    ([0, 0, 0], 0),
    ([10], 10),
    ([], "пустой"),
    ([1, 2, 3, 4, 5, 5, 5], 5),
    ([5, 5, 5, 10], 10)]
for i, (input_data, expected) in enumerate(test_cases):
    result = find_max(input_data)
    assert result == expected, f"Тест {i + 1} не пройден: ожидаемый {expected}, полученный {result}"
print("Все тесты пройдены")
