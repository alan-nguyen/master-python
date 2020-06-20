# Using recursion
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  elif n < 10:
    return n
  else: 
    last_digit = n % 10
    return last_digit + sum_digits(n // 10)

# Using iteration
## Linear - O(N), where "N" is the number of digits in the number
# def sum_digits(n):
#   if n < 0:
#     ValueError("Inputs 0 or greater only!")
#   result = 0
#   while n is not 0:
#     result += n % 10
#     n = n // 10
#   return result + n