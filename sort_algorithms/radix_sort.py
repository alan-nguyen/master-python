def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  # Create copy of to_be_sorted 
  being_sorted = to_be_sorted[:]

  # Loop over all exponents
  for exponent in range(max_exponent):
    index = - (exponent + 1)
    digits = [[] for digit in range(10)]

    # Bucket numbers
    for number in being_sorted:
      number_as_a_string = str(number)
      try: 
        digit = number_as_a_string[index]
      except IndexError:
        digit = 0
      digit = int(digit)
      digits[digit].append(number)

    # Reassign being_sorted
    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted

# TEST CASE
unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
print(f"PRE-SORT: {unsorted_list}")
print(f"POST-SORT: {radix_sort(unsorted_list)}")