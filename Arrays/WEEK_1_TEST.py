# TASK 2 Merge Sorted array
num1 = [1,2,9,0,0,0]
m = 3
num2 = [3,5,7]
n = 3

i = m-1
j= n-1
k = m+n-1

while j >=0:
  if num1[i] >=0 and num1[i] > num2[j]:
    num1[k] = num1[i]
    i -= 1
  else:
    num1[k] = num2[j]
    j -=1
  k -=1

print(num1)
  

