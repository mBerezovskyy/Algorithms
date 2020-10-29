arr_of_tuples = [(0, 1), (2, 3), (4, 7), (10, 11), (7, 10)]
# arr_of_tuples = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]



for i in range(len(arr_of_tuples)):
    arr_of_tuples[i] = list(arr_of_tuples[i])


def bubble_sort(arr):
    for iteration in range(len(arr) -1):
        for current_index in range(len(arr) - iteration - 1):
            if arr[current_index] > arr[current_index + 1]:
                arr[current_index], arr[current_index + 1] = arr[current_index + 1], arr[current_index]
    
    return arr


def sollution(arr):
    arr_sollution = []
    i = 0
    while i < len(arr) - 1:
        
        if arr[i][1] == arr[i+1][0]:
            first_el = arr[i][0]
            while i < len(arr)-1 and arr[i][1] == arr[i+1][0]:
                i += 1
            last_el = arr[i][1]
            arr_sollution.append((first_el, last_el))
            i+=1

        elif arr[i][1] > arr[i+1][0]:
            arr_sollution.append((arr[i][0], arr[i+1][1]))
            i += 1

        else:
            arr_sollution.append(tuple(arr[i]))

        i += 1
        
    return arr_sollution


print(arr_of_tuples)
print(bubble_sort(arr_of_tuples))
sorted_arr = bubble_sort(arr_of_tuples)
print(sollution(sorted_arr))