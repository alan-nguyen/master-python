def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)
  
# Helper function
def merge(left, right):
  result = []

  # Loop until left or right is empty
  while (left and right):
    if left[0] < right[0]:
      result.append(left[0]) 
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  # Merge the remain part which requires no comparision
  if left:
    result += left
  if right:
    result += right

  return result




