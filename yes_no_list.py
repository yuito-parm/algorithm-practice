numbers = [3, 7, 2, 9, 4, 10, 6]

yes_no_list = ["Yes" if num % 3 == 0 else "No" for num in numbers]

print(f"3倍の数か判定するリスト:{yes_no_list}")