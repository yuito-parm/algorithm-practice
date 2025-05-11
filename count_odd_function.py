def count_odds(numbers):
    odds_list = [num for num in numbers if num % 2 != 0]
    odd_count = len(odds_list)
    return odd_count

numbers = [3, 7, 2, 9, 4, 10, 6]

odd_count = count_odds(numbers)
print(f"奇数の個数:{odd_count}")