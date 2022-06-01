def nearest_greater_to_right(array):
  stack = []
  ans = []
  for i in range(len(array)-1,-1,-1):
    if len(stack) == 0:
      ans.append(-1)
    elif len(stack) > 0 and array[i] < stack[-1]:
      ans.append(stack[-1])
    elif len(stack) > 0 and array[i] >= stack[-1]:
      while(len(stack) > 0 and array[i] >=  stack[-1]):
        stack.pop()
      if len(stack)==0:
        ans.append(-1)
      else:
        ans.append(stack[-1])
    stack.append(array[i])
  result = ans[::-1]
  return result


array = [1,3,2,4]
print(nearest_greater_to_right(array))
