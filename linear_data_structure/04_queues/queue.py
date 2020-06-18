from node import Node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

  def peek(self):
    if self.size > 0:
      return self.head.get_value()
    else:
      print("Nothing to see here!")
  
  def get_size(self):
    return self.size
  

