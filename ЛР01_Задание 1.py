numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
none_index = numbers.index(None)
sum_without_none = 0
for num in numbers:
    if num is not None:
        sum_without_none += num

count_total = len(numbers)
average = sum_without_none / count_total
numbers[none_index] = average
print("Измененный список:", numbers)
