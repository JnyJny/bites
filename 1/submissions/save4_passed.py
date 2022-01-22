def sum_numbers(numbers=None):
    if numbers is None:
        numbers = list(range(1, 101))
    return sum(numbers)