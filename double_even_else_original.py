numbers = [3, 7, 2, 9, 4, 10, 6]

even_only_double = [num * 2 if num % 2 == 0 else num for num in numbers]

print(f"変換後のリスト:{even_only_double}")