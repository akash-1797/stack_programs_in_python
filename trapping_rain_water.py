def max_rain_trapping(arr,n):
  left_max = [0]* n
  right_max = [0] * n
  ans = 0
  left_max[0] = arr[0]
  for i in range(1,n):
    left_max[i] = max(left_max[i-1],arr[i])
  right_max[n-1] = arr[n-1]
  for i in range(n-2,-1,-1):
    right_max[i] = max(right_max[i+1],arr[i])
  for i in range(n):
    ans = ans + min(left_max[i],right_max[i]) - arr[i]
  return ans 


arr= [3,0,0,2,0,4]
n = len(arr)
print(max_rain_trapping(arr,n))
