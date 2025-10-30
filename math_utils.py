def find_max_number(num1, num2, num3):
  if (num1 > num2) and (num1 > num3):
      return num1
  if (num2 > num1) and (num2 > num3):
      return num2
  if (num3 > num1) and (num3 > num2):
      return (num3)
  if (num1==num2):
    return num1
  if (num1==num3):
    return num2
  if (num2==num3):
    return num3
    #pass  # Replace 'pass' with code

def find_mean(num1, num2, num3):
    return ((num1 + num2 + num3)/3)

import math
def find_mean_std(num1, num2, num3):
  mean1 = find_mean(num1, num2, num3)
  std = math.sqrt(((num1-mean1)**2+(num2-mean1)**2+(num3-mean1)**2)/3)
  return (mean1, std)
