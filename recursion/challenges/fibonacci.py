def fibonacci(n):
  fibs = [0, 1]
  if n <= len(fibs) - 1:
    return fibs[n]
  else:
    while n > len(fibs) - 1:
      next_fib = fibs[-1] + fibs[-2]
      fibs.append(next_fib)
  return fibs[n]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)

# Using recursion
# runtime: Exponential - O(2^N)
# def fibonacci(n):
#   if n < 0:
#     ValueError("Input 0 or greater only!")
#   if n <= 1:
#     return n
#   return fibonacci(n - 1) + fibonacci(n - 2)