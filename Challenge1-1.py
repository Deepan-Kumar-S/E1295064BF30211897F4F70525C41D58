def fact(num):
  if(num<=1):
    return 1
  else:
    return num*fact(num-1)
n = int(input("Enter Number"))
res = fact(n)
print("The factorial of ",n," is ",res)

