def binary_search(sorted_list, target):
  # Base case list is empty
  if sorted_list == []:
    return "value not found"
  mid_idx = len(sorted_list) // 2
  mid_val = sorted_list[mid_idx]
  
  # Base case found at first search
  if mid_val == target:
    return mid_idx