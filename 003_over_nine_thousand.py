def over_nine_thousand(lst):
  # Take a list of numbers 
  # Sum the elements of the list until the sum is greater than 9000.

  total = 0
  for num in lst:
    total += num
    if total > 9000:
      return total
  return total

print(over_nine_thousand([8000, 900, 120, 5000]))