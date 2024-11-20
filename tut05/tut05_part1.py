def find_triplets(arr):
  arr.sort()
  n=len(arr)
  triplets=[]
  9
  for i in range(len(arr)):
    if(i>0 and arr[i]==arr[i-1]):
      continue
    left=i+1
    right=n-1

    while(left<right):
      total = arr[i]+arr[left]+arr[right]

      if(total==0):
        triplets.append((arr[i],arr[left],arr[right]))
        left+=1
        right-=1

        while(left<right and arr[left]==arr[left-1]):
          left+=1

        while(left<right and arr[right]==arr[right+1]):
          right-=1

      elif total<0:
        left+=1

      else:
        right-=1

  return triplets


arr=[-1,0,1,2,-1,4]

find_triplets(arr)