# import heap class
from min_heap import MinHeap 
# import random number generator
from random import randrange

min_heap = MinHeap()
# print(min_heap.heap_list)

# testing out .add()
# min_heap.add(42)
# print(min_heap.heap_list)

# # populate min_heap with random numbers
# random_nums = [randrange(1, 101) for n in range(6)]
# for el in random_nums:
#   min_heap.add(el)

# # test it out, if the minimum number at index 1
# print(min_heap.heap_list)

# add elements
min_heap.add(7)
min_heap.add(12)
min_heap.add(42)

# remove minimum element
print(min_heap.retrieve_min())
