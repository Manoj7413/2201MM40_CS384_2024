students = {}

def put(name, val = []):
  name = name.lower()
  students[name] = val

def output(students):
  res = {}
  for st in students:
    sum=0
    cnt=0
    for val in students[st]:
      sum+=val
      cnt+=1

    res[st] = (sum/cnt)

  item = list(res.items())
  item.sort(key=lambda x:x[1], reverse=True)

  for key, value in item:
    print(key,'average :', value)

put("rohit",[90,89,87])
put("vipin",[76,75,37])

output(students)