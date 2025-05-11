def find_min(numbers):
    min_number = numbers[0]
    for num in numbers:
        if min_number > num:
            min_number = num
            
    return min_number

numbers = [3, 7, 2, 9, 4, 10, 6]

min_number = find_min(numbers)
print(f"最小値:{min_number}")