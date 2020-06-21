def binary_search(sorted_list, left_pointer, right_pointer, target):
  # this condition indicates it reached an empty "sub-list"
  if left_pointer >= right_pointer:
    return "value not found"
	
  # Calculate the middle index from the pointers 
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]

  if mid_val == target:
    return mid_idx
  if mid_val > target:
    # Reduce the sub-list by passing in a new right_pointer
    return binary_search(sorted_list, left_pointer, mid_idx, target)
  if mid_val < target:
    # Reduce the sub-list by passing in a new left_pointer
    return binary_search(sorted_list, mid_idx + 1, right_pointer, target)

