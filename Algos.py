from math import inf

numbers = [
    42, -7, 0, 15, 15, 99, -100, 3, 8, 1,
    50, 23, -2, 76, 4, 4, 88, 12, -45, 67,
    2, 1000, -999, 31, 6, 19, 19, 54, 11, 5,
    90, -1, 33, 27, 72, 10, 10, 41, 64, 7,
    25, -20, 500, 14, 3, 81, 18, 0, 37, 60
]

non_numbers = ['cat', 'dog', 'mouse', 'lion']

floaters = [42.2, -7, 0, 15.5, 15, 99, -100.1, 42, 8.8, 1]

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

def two_num_sum(numbers, target_value):
    target = target_value
    combinations = []
    if numbers:
        for number in numbers:
            goal_number = target - number
            if goal_number == number and numbers.count(number) > 1 and (goal_number, number) not in combinations:
                combinations.append((goal_number, number))
                
            elif goal_number in numbers and (goal_number, number) not in combinations and (number, goal_number) not in combinations and goal_number != number:
                combinations.append((goal_number, number))

            else:
                continue
        if combinations:
            return combinations
        else:
            return 'No combination found'
    return 'Empty List'

print(two_num_sum([1, 4], 8))