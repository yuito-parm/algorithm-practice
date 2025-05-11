def find_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
            
    return max_number

def find_min(numbers):
    min_number = numbers[0]
    for num in numbers:
        if min_number > num:
            min_number = num
            
    return min_number

def get_range(numbers):
    max_number = find_max(numbers)
    min_number = find_min(numbers)
    diff = max_number - min_number
    
    return diff

numbers = [3, 7, 2, 9, 4, 10, 6]
 
diff = get_range(numbers)
print(f"最大と最小値の差:{diff}")