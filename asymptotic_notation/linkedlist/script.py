from linkedlist import LinkedList

def find_max(linked_list):
  print("--------------------------")
  print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))
  current = linked_list.get_head_node()
  max_value = current.get_value()
  while current.get_next_node():
    current = current.get_next_node()
    if current.get_value() > max_value:
      max_value = current.get_value()
  return max_value
  
  

