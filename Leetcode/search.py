from template.search import exponential_search, binary_search, linear_seach, jump_search
from time import perf_counter
start = perf_counter()
index = exponential_search(range(1,1000000000), 999564)
end = perf_counter()
print(index, "Exponential Time : ", end-start)

start = perf_counter()
index = jump_search(range(1,1000000000), 999564)
end = perf_counter()
print(index, "Jump Time : ", end-start)

start = perf_counter()
index = binary_search(range(1,1000000000), 999564)
end = perf_counter()
print(index, "Binary Time : ", end-start)

start = perf_counter()
index = linear_seach(range(1,1000000000), 999564)
end = perf_counter()
print(index, "Linera Time : ", end-start)