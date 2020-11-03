"""
first training input
"""
input_array1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

"""
second training input (my own)
"""
input_array2 = [(0, 1), (4, 7), (2, 3), (10, 11), (7, 10)]


def merge_sort(array):
    """
    returns sorted array


    >>> merge_sort(input_array1)
    [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]

    >>> merge_sort(input_array2)
    [(0, 1), (2, 3), (4, 7), (7, 10), (10, 11)]
    """

    if len(array) == 1:
        return

    middle_index = len(array) // 2

    left_subarray = array[:middle_index]
    right_subarray = array[middle_index:]

    merge_sort(left_subarray)
    merge_sort(right_subarray)

    left_subarray_index, right_subarray_index, final_array_index = 0, 0, 0

    while left_subarray_index < len(left_subarray) and right_subarray_index < len(right_subarray):
        if left_subarray[left_subarray_index] < right_subarray[right_subarray_index]:
            array[final_array_index] = left_subarray[left_subarray_index]
            left_subarray_index += 1

        else:
            array[final_array_index] = right_subarray[right_subarray_index]
            right_subarray_index += 1

        final_array_index += 1

    while left_subarray_index < len(left_subarray):
        array[final_array_index] = left_subarray[left_subarray_index]
        final_array_index += 1
        left_subarray_index += 1

    while right_subarray_index < len(right_subarray):
        array[final_array_index] = right_subarray[right_subarray_index]
        final_array_index += 1
        right_subarray_index += 1

    return array


def solution(array):
    """
    returns output_array which is a solution to given task

    best - O(N)
    worst - O(N^2)


    >>> solution(merge_sort(input_array1))
    [(0, 1), (3, 8), (9, 12)]

    >>> solution(merge_sort(input_array2))
    [(0, 1), (2, 3), (4, 11)]
    """
    output_array = []
    index = 0
    while index < len(array) - 1:

        if array[index][1] == array[index + 1][0]:
            first_el = array[index][0]
            while index < len(array) - 1 and array[index][1] == array[index + 1][0]:
                index += 1
            second_el = array[index][1]
            output_array.append((first_el, second_el))
            index += 1

        elif array[index][1] > array[index + 1][0]:
            output_array.append((array[index][0], array[index + 1][1]))
            index += 1

        else:
            output_array.append(tuple(array[index]))

        index += 1

    return output_array


if __name__ == "__main__":
    import doctest
    doctest.testmod()