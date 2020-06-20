def flatten(my_list):
  result = []
  for e in my_list:
    if isinstance(e, list):
      print("List found!")
      flat_list = flatten(e)
      result += flat_list
    else:
      result.append(e)
  return result

# Test case
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))