class TreeNode:
  def __init__(self, value):
    print('initializing node...')
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print('Adding ' + child_node.value)
    self.children.append(child_node)

  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    # new_children = []
    # for child in self.children:
    #   if child != child_node:
    #     new_children.append(child)
    # self.children = new_children
    self.children = [child for child in self.children if child != child_node]

  def traverse(self):
    print(self.value)
    for child in self.children:
      print(child.value)

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")

root.add_child(first_child)
root.add_child(second_child)
root.traverse()

# root = TreeNode("I am Root")
# child = TreeNode("A wee sappling")

# Create an instance
# root = TreeNode("I am Root")
# child = TreeNode("A wee sappling")
# root.add_child(child)
# bad_seed = TreeNode("Root Rot!")
# root.add_child(child)
# root.add_child(bad_seed)
# root.remove_child(bad_seed)