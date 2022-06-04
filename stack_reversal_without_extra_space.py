def insert(stack,ele):
  if len(stack) == 0:
    stack.append(ele)
    return
  temp = stack.pop()
  insert(stack,ele)
  stack.append(temp)
  return stack


def reverse_a_stack(stack):
  if len(stack) == 0:
    return
  if len(stack) == 1:
    return
  temp_1 = stack.pop()
  reverse_a_stack(stack)
  insert(stack,temp_1)
  return stack



stack = [1,2,3,4,5,6,67]
x = reverse_a_stack(stack)
print(x)
print(id(x))
print(id(stack))

