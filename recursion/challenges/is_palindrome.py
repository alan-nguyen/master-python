# ----------------- Strategy ---------------------
# BASE CASE
# the input string is less than 2 characters
  # return True
# RECURSIVE STEP
# str[0] does not match str[-1]
  # return False
# return recursive call with str[1:-1]

def is_palindrome(my_string):
  if len(my_string) < 2:
    return True
  else:
    if my_string[0] != my_string[-1]:
      return False
    return is_palindrome(my_string[1:-1])


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)


# # Quadratic - O(N^2)
# def is_palindrome(my_string):
#   while len(my_string) > 1:
#     if my_string[0] != my_string[-1]:
#       return False
#     my_string = my_string[1:-1]
#   return True 

# palindrome("abba")
# # True
# palindrome("abcba")
# # True
# palindrome("")
# # True
# palindrome("abcd")
# # False

# # Linear - O(N)
# def is_palindrome(my_string):
#   string_length = len(my_string)
#   middle_index = string_length // 2
#   for index in range(0, middle_index):
#     opposite_character_index = string_length - index - 1
#     if my_string[index] != my_string[opposite_character_index]:
#       return False  
#   return True