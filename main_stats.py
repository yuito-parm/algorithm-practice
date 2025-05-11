from stats_utils import find_max, find_min, get_average, get_range

with open("numbers.txt", "r") as f:
    numbers = [int(line) for line in f]

max_number = find_max(numbers)
min_number = find_min(numbers)
average = get_average(numbers)
diff = get_range(numbers)

print(f"最大値:{max_number}")
print(f"最小値:{min_number}")
print(f"平均値:{average}")
print(f"最大値と最小値の差:{diff}")