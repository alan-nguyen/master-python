#Linear Search Algorithm
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches != []:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))

# Test case for duplicating 
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)

#Finding the Maximum Value
def find_max(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if maximum_score_index is None or search_list[idx] > maximum_score_index:
      maximum_score_index = idx
  return maximum_score_index

