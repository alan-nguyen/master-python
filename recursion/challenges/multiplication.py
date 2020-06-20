# --------- Strategy -------------
# BASE CASE
# if either input is 0, return 0
# RECURSIVE STEP
# return one input added to a recursive call with the OTHER input decremented by 1

def multiplication(num_1, num_2):
  if num_1 == 0 or num_2 == 0:
    return 0
  else: 
    return num_2 + multiplication(num_1 - 1, num_2)


# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)

# Using iteration
# def multiplication(num_1, num_2):
#   result = 0
#   for count in range(0, num_2):
#     result += num_1
#   return result