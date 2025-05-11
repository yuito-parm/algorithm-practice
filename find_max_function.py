def find_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
            
    return max_number

numbers = [3, 7, 2, 9, 4, 10, 6]

max_number = find_max(numbers)
print(f"最大値:{max_number}")