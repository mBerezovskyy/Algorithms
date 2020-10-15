import time


class MergeSort:
    number_of_comparisons = 0

    @staticmethod
    def sort_ascending(array, key=lambda obj: obj):
        start_time = time.time()

        if len(array) == 1:
            return

        middle_index = len(array) // 2

        left_subarray = array[:middle_index]
        right_subarray = array[middle_index:]

        MergeSort.sort_ascending(left_subarray)
        MergeSort.sort_ascending(right_subarray)

        left_subarray_index, right_subarray_index, final_array_index = 0, 0, 0
        while left_subarray_index < len(left_subarray) and right_subarray_index < len(right_subarray):
            MergeSort.number_of_comparisons += 2
            if key(left_subarray[left_subarray_index]) < key(right_subarray[right_subarray_index]):
                MergeSort.number_of_comparisons += 1
                array[final_array_index] = left_subarray[left_subarray_index]
                left_subarray_index += 1

            else:
                array[final_array_index] = right_subarray[right_subarray_index]
                right_subarray_index += 1

            final_array_index += 1

        while left_subarray_index < len(left_subarray):
            MergeSort.number_of_comparisons += 1
            array[final_array_index] = left_subarray[left_subarray_index]
            final_array_index += 1
            left_subarray_index += 1

        while right_subarray_index < len(right_subarray):
            MergeSort.number_of_comparisons += 1
            array[final_array_index] = right_subarray[right_subarray_index]
            final_array_index += 1
            right_subarray_index += 1

        end_time = time.time()

        return f'Merge sort\n' \
               f'time: {end_time - start_time}\n' \
               f'number of comparisons: {MergeSort.number_of_comparisons}\n' \
               f'sorted array: {array}'
