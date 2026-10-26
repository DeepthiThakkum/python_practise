def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


multiply(2, 3, 4, 5)
