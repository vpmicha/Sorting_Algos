from math import inf
from timeit import timeit

numbers = [
    42, -7, 0, 15, 15, 99, -100, 3, 8, 1,
    50, 23, -2, 76, 4, 4, 88, 12, -45, 67,
    2, 1000, -999, 31, 6, 19, 19, 54, 11, 5,
    90, -1, 33, 27, 72, 10, 10, 41, 64, 7,
    25, -20, 500, 14, 3, 81, 18, 0, 37, 60
]

non_numbers = ['cat', 'dog', 'mouse', 'lion']

floaters = [42.2, -7, 0, 15.5, 15, 99, -100.1, 42, 8.8, 1]

def avg_time(function):
    reps = 1000000
    time_taken = timeit(function, number=reps)
    return f'{round((time_taken / reps)*10**6, 2)} micro-seconds'

def largest_number(numbers):
    found_number = False
    if numbers:
        number = numbers[0]
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

def second_largest_number(numbers):
    found_number = False
    if numbers:
        largest = -inf
        second_largest = numbers[0]
        for i in numbers:
            try:
                if i > largest:
                    second_largest = largest
                    largest = i
                    found_number = True
                if second_largest < i < largest:
                    second_largest = i
                    
            except TypeError:
                print(f'List contained non number {i}')
                continue

        if second_largest == -inf:
            return None

        if not found_number:
            return 'List did not contain any numbers'

        return second_largest

    else:
        return 'Empty list'

def smallest_largest(numbers):
    found_number = False
    if numbers:
        largest = -inf
        smallest = +inf
        for i in numbers:
            try:
                if i > largest:
                    largest = i
                    found_number = True
                
                if i < smallest:
                    smallest = i
                    found_number = True

            except TypeError:
                print(f'List contained non number {i}')
                continue

        if not found_number:
            return 'List did not contain any numbers'

        return (smallest, largest)

    else:
        return 'Empty list'

def value_count(numbers):
    count_dict = {}
    if numbers:
        first_time = True
        for number in numbers:
            if number not in count_dict:
                count_dict[number] = 1
            elif number in count_dict:
                count_dict[number] += 1
    else:
        return 'Empty list'

    return count_dict

def two_num_sum(numbers, target):
    combinations = []
    numbers_set = set()

    if numbers:
        for number in numbers:
            diff = target - number
            if diff in numbers_set:
                combinations.append((number,diff))
            else:
                numbers_set.add(number)
        if combinations:
            return combinations
        else:
            return 'No combination found'

    return 'Empty list'

print(avg_time(lambda: two_num_sum([4, 7, 1, 9, 3, 6, 12, -2, 8], 10)))
