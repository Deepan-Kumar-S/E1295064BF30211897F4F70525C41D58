def isLeapyear(year):
  if((year % 4 == 0 and year % 100 !=0) or year %400 == 0):
    return True
  else:
    return False

y = int(input("Enter Year: "))
if(isLeapyear(y)):
  print(y," is a Leap Year")
else:
  print(y," is not a Leap Year")