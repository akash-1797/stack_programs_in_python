class Stack:
  def __init__(self):
    self.arr = []
    self.support_stack = []
  def push(self,ele):
    self.arr.append(ele)
    if len(self.support_stack) == 0 or ele <= self.support_stack[-1]:
      self.support_stack.append(ele)
      return
  def pop(self):
    if len(self.support_stack) ==0:
      return -1
    ans  = self.arr.pop()
    if ans == self.support_stack[-1]:
      self.support_stack.pop()
    return ans
  def get_min(self):
    if len(self.support_stack) == 0:
      return -1
    return self.support_stack[-1]

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(1)
s.push(0)
s.push(-1)
s.pop()
s.pop()
print(s.get_min())
