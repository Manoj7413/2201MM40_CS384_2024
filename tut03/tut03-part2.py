def strr(s):
  nu=len(s)
  vec=[0]*nu

  print(s)

  str = list(s)
  i=0
  while i<nu:
    if vec[i]<i:
      if i%2==0:
        str[0],str[i]=str[i],str[0]
      else:
        str[vec[i]],str[i]=str[i],str[vec[i]]
      print(''.join(str))
      vec[i]+=1
      i=0
    else:
      vec[i]=0
      i+=1

strr('ABC')