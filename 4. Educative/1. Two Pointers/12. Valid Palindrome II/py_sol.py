def is_palind(s):
  s = s.lower()
  left = 0
  right = len(s)-1
  # Replace this placeholder return statement with your code
  while left < right:
    if s[left] != s[right]:
      return False
    left+=1
    right-=1
  return True

def is_palindrome(s):
  s = s.lower()
  left = 0
  right = len(s)-1
  while left<right:
    if s[left] != s[right]:
      if is_palind(s[left:right]) or is_palind(s[left+1:right+1]):
        return True
      else:
        return False
    left+=1
    right-=1
  return True