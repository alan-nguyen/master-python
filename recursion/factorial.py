def factorial(n):
  if n == 1:
    return n
  else:
    return factorial(n-1) * n

# Test case
print(factorial(12))