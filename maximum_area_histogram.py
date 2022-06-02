def fun_l(arr):
  n = len(arr)
  stack = []
  for i in range(0,n):
    if len(stack) == 0:
      left[i] = 0
      stack.append(i)
    while(len(stack) > 0 and arr[stack[-1]] >= arr[i]):
      stack.pop()
    if len(stack) == 0:
      left[i] = 0
    else:
      left[i] = stack[-1]+1
    stack.append(i)
  return left

def fun_r(arr):
  n = len(arr)
  stack = []
  for i in range(len(arr)-1,-1,-1):
    if len(stack) == 0:
      right[i] = n-1
      stack.append(i)
    while(len(stack) > 0 and arr[stack[-1]] >= arr[i]):
      stack.pop()
    if len(stack) == 0:
      right[i] = n-1
    else:
      right[i] = stack[-1]-1
    stack.append(i)
  return right

arr = [7,2,8,9,1,3,6,5]
left = [0]* len(arr)
right = [0] * len(arr)
l = fun_l(arr)
r = fun_r(arr)
ans = [0] * len(arr)
for i in range(0,len(arr)):
  ans[i] = r[i]-l[i]+1
print(ans)
max_1 = [0] * len(arr)
for i in range(0,len(arr)):
  max_1[i] = ans[i] * arr[i]
print(max_1)
print(max(max_1))

