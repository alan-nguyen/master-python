class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0
  
  def retrieve_min(self): 
    if self.count == 0:
      print("No items in heap")
      return None
    min = self.heap_list[1]
    print(f"Removing: {min} from {self.heap_list}")
    self.heap_list[1] = self.heap_list[self.count]
    self.heap_list[self.count] = min
    self.heap_list.pop()
    self.count -= 1
    print(f"Last element moved to fisrt: {self.heap_list}")
    self.heapify_down()
    return min
  
  def add(self, element):
    print(f"Adding {element} to {self.heap_list}")
    self.count += 1
    self.heap_list.append(element)
    self.heapify_up()

  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      print('There is only a left child')
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child < right_child:
        print(f"{left_child} is smaller than {right_child}")
        return self.left_child_idx(idx)
      else:
        print(f"{right_child} is smaller than {left_child}")
        return self.right_child_idx(idx)
        
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

  def heapify_down(self):
    print("Heapifying down! {incomplete}")
    idx = 1 