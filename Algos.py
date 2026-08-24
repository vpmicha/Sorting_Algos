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

def largest_number(list):
    found_number = False
    if list:
        number = list[0]
        for i in list:
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

def second_largest_number(list):
    found_number = False
    if list:
        largest = -inf
        second_largest = list[0]
        for i in list:
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

def smallest_largest(list):
    found_number = False
    if list:
        largest = -inf
        smallest = +inf
        for i in list:
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

def value_count(list):
    count_dict = {}
    if list:
        first_time = True
        for number in list:
            if number not in count_dict:
                count_dict[number] = 1
            elif number in count_dict:
                count_dict[number] += 1
    else:
        return 'Empty list'

    return count_dict

def two_num_sum(list, target_value):
    target = target_value
    sum_list = list
    if list:
        first = list[0]
        second = sum_list[0]
        first_index = list.index(first)
        first_loop_iterations = 0
        second_loop_iterations = 0
        while True:
            for i in list[first_index:]:
                first = i
                first_loop_iterations += 1
                break
            for j in sum_list:
                second = j
                second_loop_iterations += 1
                if first + second == target and first_loop_iterations != second_loop_iterations:
                    return (first, second)
            second_loop_iterations = 0
            first_index += 1

            if first_loop_iterations == len(list):
                break

        return 'No combination found'
    return 'Empty list'

[4, 6, 3, 6, 1, 7]                   
[4, 6, 3, 6, 1, 7]                   
                

print(two_num_sum([4, 6, 3, 1, 1, 7], 12))