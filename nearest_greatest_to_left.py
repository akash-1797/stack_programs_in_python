def nearest_greatest_to_left(array):
  stack = []
  ans = []
  for i in range(0,len(array)):
    if len(stack) == 0:
      ans.append(-1)
    elif len(stack)> 0 and array[i] < stack[-1]:
      ans.append(stack[-1])
    elif len(stack)> 0 and array[i] >= stack[-1]:
      while(len(stack) > 0 and array[i] >= stack[-1]):
        stack.pop()
      if len(stack) == 0:
        ans.append(-1)
      else:
        ans .append(stack[-1])
    stack.append(array[i])
  return ans 

array = [1,3,2,4]
print(nearest_greatest_to_left(array))
