class Stack:
  def __init__(self):
    self.data = []
  
  def push(self,ele):
    self.data.append(ele)
    return
  
  def pop(self):
    if self.is_empty():
      return "hey stack is empty"
    else:
     return self.data.pop()
  
  def is_empty(self):
    if len(self.data) == 0:
      return True
    else:
      return False
    
  def size(self):
    return len(self.data)
  
  def top(self):
    if self.is_empty() == True:
      return 'hey the stack is empty'
    else:
      return self.data[len(self.data)-1]

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
while(s.is_empty() is False):
  print(s.pop())
print(s.top())
s.push(10)
s.push(20)
s.push(30)
print(s.top())
