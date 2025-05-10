numbers = [3, 7, 2, 9, 4, 10, 6]

max_number = numbers[0]
min_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num
    elif min_number > num:
        min_number = num

diff = max_number - min_number

print(f"最大値と最小値の差:{diff}")