def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  return max_exponent
  
  # create copy of to_be_sorted 
  being_sorted = to_be_sorted[:]
  digits = [[] for digit in range(10)]
  return digits