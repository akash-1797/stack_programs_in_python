class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.count = 0

  def push(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.count += 1
    else:
      new_node.next = self.head
      self.head = new_node 
      self.count += 1
      return 
  def pop(self):
    if self.is_empty() == True:
      print('hey stack is empty')
    else:
      popped_item = self.head.data
      self.head = self.head.next
      self.count -= 1
    return popped_item

  def size(self):
    return self.count 


  def top(self):
    if self.is_empty() == True:
      return 'hey stack is empty'
    else:
      return self.head.data


  def is_empty(self):
    if self.count ==0 :
      return True
    else:
      return False


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
while(s.is_empty() is False):
  print(s.pop())
print(s.top())
s.push(10000)
print(s.top())

