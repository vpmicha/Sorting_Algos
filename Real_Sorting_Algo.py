from Algos import avg_time

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

print(avg_time(lambda: two_num_sum(list(range(100)), 197)))