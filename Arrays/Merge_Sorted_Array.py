num1 = [1,2,4,0,0,0]
m = 3
num2 = [3,5,6]
n = 3
# num1_end = m-1
# num2_end = n-1
# insert_pos = m+n-1

# while num2_end >= 0:
#   if num1[num1_end] >=0 and num1[num1_end] > num2[num2_end]:
#     num1[insert_pos] = num1[num1_end]
#     num1_end -=1
#   else:
#     num1[insert_pos] = num2[num2_end]
#     num2_end -=1
#   insert_pos -=1
# print(num1)

# I want to apply job for Data Scientist 

for i in range(m):
  num1[m+i] = num2[i]

num1.sort()
print(num1)