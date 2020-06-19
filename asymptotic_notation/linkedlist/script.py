from linkedlist import LinkedList

# Pseudo code for find_max
# - set a variable, current, equal to the head node of the linked list
# - set the maximum to the value of current
# - while current has a next node
#     - set current to the next node of current
#     - if current's value is greater than the maximum, set maximum to current's value

# - return maximum
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
  

# #Test Cases for find_max
# ll = LinkedList(6)
# ll.insert_beginning(32)
# ll.insert_beginning(-12)
# ll.insert_beginning(48)
# ll.insert_beginning(2)
# ll.insert_beginning(1)
# print("The maximum value in this linked list is {0}\n".format(find_max(ll)))

# ll_2 = LinkedList(60)
# ll_2.insert_beginning(12)
# ll_2.insert_beginning(22)
# ll_2.insert_beginning(-10)
# print("The maximum value in this linked list is {0}\n".format(find_max(ll_2)))

# ll_3 = LinkedList("A")
# ll_3.insert_beginning("X")
# ll_3.insert_beginning("V")
# ll_3.insert_beginning("L")
# ll_3.insert_beginning("D")
# ll_3.insert_beginning("Q")
# print("The maximum value in this linked list is {0}\n".format(find_max(ll_3)))

# #Runtime of find_max
# runtime = "N"
# print("The runtime of find_max is O({0})".format(runtime))
# # END of find_max

def sort_linked_list(linked_list):
  print("\n---------------------------")
  print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
  new_linked_list = LinkedList()
  #Write Code Here!
  while linked_list.get_head_node():
    max_val = find_max(linked_list)
    new_linked_list.insert_beginning(max_val)
    linked_list.remove_node(max_val)
  return new_linked_list
