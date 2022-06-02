def countRev (s):
    l = len(s)
    count = 0
    if l % 2 != 0:
        return -1
    stack = []
    for char in s:
        if char == "{":
            stack.append(char)
        else:
            if len(stack) == 0:
                count = count +1
                stack.append('{')
            else:
                stack.pop()
    count = count + (len(stack)//2)
    return count
