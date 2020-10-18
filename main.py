from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort

import time

from utils.csv_to_list import csv_to_list

insertion_sort = InsertionSort()
merge_sort = MergeSort()


list_of_squeezers = csv_to_list()

list_of_squeezers_productivity = [item.productivity_in_litres_per_hour for item in list_of_squeezers]
list_of_squeezers_power = [item.power_consumption_in_kilowatts for item in list_of_squeezers]

start = time.time()
print(insertion_sort.descending_sort(list_of_squeezers_productivity))
end = time.time()
print(f"time:{end-start}")
print('-'*30)
start = time.time()
print(merge_sort.sort_ascending(list_of_squeezers_power))
end = time.time()
print(f"time:{end-start}")
