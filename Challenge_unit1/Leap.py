def LeapYear(year):
  if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    return True
  else:
    return False


year = int(input("Enter the Year: "))
if LeapYear(year):
  print("{} is a Leap Year".format(year))
else:
  print("{} is not a Leap Year".format(year))
