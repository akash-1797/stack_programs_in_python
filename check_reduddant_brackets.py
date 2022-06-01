def check_duplicate_brackets(string):
  stack = []
  l = len(string)
  if l == 0 or l ==1:
    return False
  for char in string:
    if(char == '+' or char == "-" or char == "*" or char == "/" or char == '('):
      stack.append(char)
    elif char == ")":
      if stack[-1] == '(':
        return True
      else:
        while(stack[-1] != "("):
          stack.pop()
        stack.pop()
  return False

string = "(a+b)"
string_1 = "a+b*((a/c-d)))"
print(check_duplicate_brackets(string_1))

