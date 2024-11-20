def prime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5+1)):
    if n%i==0:
      return False
  return True

def permutation(n):
  strr=str(n)
  s=[int(strr[i:]+strr[:i]) for i in range(len(strr))]
  return s

def check(n):
  for p in permutation(n):
    if not prime(p):
      return False
  return True

if not check(23):
  print('given number is not a rotational prime number')
else:
  print('given number is a rotational prime number')