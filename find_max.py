numbers = [3, 7, 2, 9, 4, 10, 6]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num


print(f"最大値:{max}")