class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    stack = []  # unpaired '(' indices
    chars = [c for c in s]

    for i, c in enumerate(chars):
      if c == '(':
        stack.append(i)  # Record the unpaired '(' index.
      elif c == ')':
        if stack:
          stack.pop()
        else:
          chars[i] = '*'  
    while stack:
      chars[stack.pop()] = '*'

    return ''.join(chars).replace('*', '')