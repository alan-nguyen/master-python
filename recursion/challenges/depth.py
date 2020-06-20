# --------- Strategy --------------
# function takes "tree_node" as input
  # BASE CASE
  # if tree_node is None
    # return 0
  # RECURSIVE STEP
  # set left_depth to recursive call passing tree_node's left child
  # set right_depth to recursive call passing tree_node's right child

  # if left_depth is greater than right depth:
    # return left_depth + 1
  # else
    # return right_depth + 1
    
def depth(tree_node):
  if tree_node is None:
    return 0
  else:
    left_depth = depth(tree_node["left_child"])
    right_depth = depth(tree_node["right_child"])
    if left_depth > right_depth:
      return left_depth + 1
    else:
      return right_depth + 1


# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)

# Using iteration
# def depth(tree):
#   result = 0
#   # our "queue" will store nodes at each level
#   queue = [tree]
#   # loop as long as there are nodes to explore
#   while queue:
#     # count the number of child nodes
#     level_count = len(queue)
#     for child_count in range(0, level_count):
#       # loop through each child
#       child = queue.pop(0)
#      # add its children if they exist
#       if child["left_child"]:
#         queue.append(child["left_child"])
#       if child["right_child"]:
#         queue.append(child["right_child"])
#     # count the level
#     result += 1
#   return result