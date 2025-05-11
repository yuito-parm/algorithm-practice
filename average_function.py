def get_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

numbers = [3, 7, 2, 9, 4, 10, 6]

average = get_average(numbers)
print(f"平均値:{average}")
print(f"平均値:{average:.1f}(小数点以下丸め版)")