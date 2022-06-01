def stock_span(array,ans):
  stack = []
  ans.append(1)
  stack.append(0)
  for i in range(1,len(array)):
    while(len(stack) > 0  and array[i] > array[stack[-1]]):
      stack.pop()
    if len(stack) == 0:
      x = i+1
      ans.append(x)
    else:
      h = i - stack[-1]
      ans.append(h)
    stack.append(i)
  return ans
        
        

array = [60,70,80,100,90,75,80,120]
ans = []
print(stock_span(array,ans))

      
