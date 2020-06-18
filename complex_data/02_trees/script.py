class TreeNode:
  def __init__(self, value):
    print('initializing node...')
    self.value = value

  def add_child(self, child_node):
    print('Adding ' + child_node.value)
    self.children.append(child_node)

