def reverse_stack(inputstack,outputstack):
  if len(inputstack) == 0:
    return
  if len(inputstack) == 1:
    return 
  var_1 = inputstack.pop()
  reverse_stack(inputstack,outputstack)
  for i in range(0,len(inputstack)):
    x = inputstack.pop()
    outputstack.append(x)

  inputstack.append(var_1)
  
  for i in range(0,len(outputstack)):
    x = outputstack.pop()
    inputstack.append(x)
  return inputstack


s1 = [2,3,4,5,6,7,8,9,0,11,12]
s2 = []
s3 = reverse_stack(s1,s2)
print(id(s1))
print(id(s3))
print(s3)

