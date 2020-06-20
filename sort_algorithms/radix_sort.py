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
      digit = number_as_a_string[index]
      digit = int(digit)
      digits[digit].append(number)

    # Reassign being_sorted
    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted
