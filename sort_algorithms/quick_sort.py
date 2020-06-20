# use randrange to produce a random index
from random import randrange

def quicksort(list, start, end):
  if start >= end:
    return list
	# Define your pivot variables below
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  # Swap the elements in list below
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  
