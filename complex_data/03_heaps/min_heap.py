class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0
  
  def add(self, element):
    print(f"Adding {element} to {self.heap_list}")
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()

  # HEAP HELPER METHODS
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def heapify_up(self):
    print("Heapifying up")
    # start at the last element of the list
    # while there's a parent element available:
        # if the parent element is greater:
          # swap the elements
        # set the target element index to be the parent's index
    idx = self.count
    while self.parent_idx(idx) > 0:
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent > child:
        print(f"swapping {parent} with {child} ")
        self.heap_list[self.parent_idx(idx)] = child
        self.heap_list[idx] = parent
      idx = self.parent_idx(idx)
    print(f"Heap Restored {self.heap_list}")