# --------- Strategy ---------------------------------
# function definition with two inputs: 
# a list and a min that defaults to None
  # BASE CASE
  # if input is an empty list
    # return min
  # else
    # RECURSIVE STEP
    # if min is None
    # OR
    # first element of list is < min
      # set min to be first element
  # return recursive call with list[1:] and the min

def find_min(my_list, min=None):
  if len(my_list) == 0:
    return min
  else:
    if min is None or my_list[0] < min:
      min = my_list[0]
  return find_min(my_list[1:], min)

# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)

# Using iteration
# def find_min(my_list):
#   min = None
#   for element in my_list:
#     if not min or (element < min):
#       min = element
#   return min

# find_min([42, 17, 2, -1, 67])
# # -1
# find_mind([])
# # None
# find_min([13, 72, 19, 5, 86])
# # 5