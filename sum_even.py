numbers = [3, 7, 2, 9, 4, 10, 6]

even_total = 0
for num in numbers:
    if num % 2 == 0:
        even_total += num

print(f"偶数の合計:{even_total}")