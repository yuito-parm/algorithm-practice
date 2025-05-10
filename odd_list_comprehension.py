numbers = [3, 7, 2, 9, 4, 10, 6]

odd_list = [num for num in numbers if num % 2 != 0]

odd_count = len(odd_list)
print(f"奇数のリスト:{odd_list}")
print(f"奇数の個数:{odd_count}")