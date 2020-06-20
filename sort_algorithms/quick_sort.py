# use randrange to produce a random index
from random import randrange

def quicksort(list, start, end):
  if start >= end:
    return list
	# Define pivot variables 
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  # Swap the elements in list 
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  # Create the lesser_than_pointer
  lesser_than_pointer = start
  for idx in range(start, end):
    if list[idx] < pivot_element:
      list[lesser_than_pointer], list[idx] = list[idx], list[lesser_than_pointer]
      lesser_than_pointer += 1
  # After the loop is finished...
  # swap pivot with value at lesser_than_pointer
  list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]
  print(list[start])
  start += 1
  return quicksort(list, start, end)
