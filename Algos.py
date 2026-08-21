from math import inf
import numbers


numbers = [
    42, -7, 0, 15, 15, 99, -100, 3, 8, 1,
    50, 23, -2, 76, 4, 4, 88, 12, -45, 67,
    2, 1000, -999, 31, 6, 19, 19, 54, 11, 5,
    90, -1, 33, 27, 72, 10, 10, 41, 64, 7,
    25, -20, 500, 14, 3, 81, 18, 0, 37, 60
]
non_numbers = ['cat', 'dog', 'mouse', 'lion']

def largest_number(numbers):
    found_number = False
    if numbers:
        number = -inf
        for i in numbers:
            try:
                if i >= number:
                    number = i
                    found_number = True

            except TypeError:
                print(f'List contained non number {i}')
                continue
        if not found_number:
            number = 'List did not contain any numbers'

    else:
        return 'Empty list'

    return number

print(largest_number(numbers))

