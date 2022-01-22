def sum_numbers(numbers=None):
    if numbers is None:
        number = list(range(1, 101))
    return sum(numbers)