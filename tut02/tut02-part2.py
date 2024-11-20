def solve(s):
  ans=""
  i = 0

  while(i<len(s)):
    current_char=s[i]
    ct=1

    while(i<len(s)-1 and s[i]==s[i+1]):
       ct+=1
       i+=1

    ans+=current_char+str(ct)
    i+=1

  return ans

user_input = input("Enter a string: ")
ans = solve(user_input)
print(ans)