numbers = [3, 7, 2, 9, 4, 10, 6]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)
print(f"平均値:{average:.1f}")