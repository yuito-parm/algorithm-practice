numbers = [3, 7, 2, 9, 4, 10, 6]

min_number = numbers[0]
for num in numbers:
    if min_number > num:
        min_number = num

print(f"最小値:{min_number}")