def label_numbers(numbers):
    labels = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

    return labels


label_nums = label_numbers([1, 2, 3, 4, 5])
print(label_nums)