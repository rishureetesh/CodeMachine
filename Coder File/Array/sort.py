from Sorting import insertion_sort, bubble_sort, selection_sort
from time import perf_counter
start = perf_counter()
index = insertion_sort([1,5,3,4,6,2,7,9,10,7])
end = perf_counter()
print(index, "Insertion Sort Time : ", end-start)

start = perf_counter()
index = bubble_sort([1,5,3,4,6,2,7,9,10,7])
end = perf_counter()
print(index, "Bubble Sort Time : ", end-start)

start = perf_counter()
index = selection_sort([1,5,3,4,6,2,7,9,10,7])
end = perf_counter()
print(index, "Selection Sort Time : ", end-start)