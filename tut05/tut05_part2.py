def is_balanced(s):
  arr=[]
  match={')':'(','}':'{',']':'['}

  for char in s:
    if char in match.values():
      arr.append(char)

    elif char in match.keys():
      if arr==[] or match[char]!=arr.pop():
        return "The input String is NOT balanced"

  if arr==[]:
    return "The input String is balanced"

  else:
    return "The input String is NOT balanced"

s="[{()}"
is_balanced(s)