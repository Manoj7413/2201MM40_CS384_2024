def totalsum(n):
  while(n>=10):
    digit_sum=0
    current_num=n

    while(current_num>0):
      last_digit=current_num%10
      digit_sum=digit_sum+last_digit
      current_num=int(current_num//10)

    n = digit_sum

  return n

num = int(input("Enter an integer: "))
print(totalsum(num))