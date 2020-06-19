def sum_to_one(n):
  if n == 1:
    return n
  else:
    print(f"Recursing with input: {n}")
    return sum_to_one(n-1) + n
print(sum_to_one(7))