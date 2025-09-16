# nums = [1,2,3,4]
# answer = []
# result = 1
# length = len(nums)
# for i in range(length):
#   for j in range(length):
#     if i == j:
#       continue
#     else:
#       result *=nums[j]
#   answer.append(result)
#   result = 1

# print(answer)


# 2nd Approach

nums = [1,2,3,4]
length = len(nums)
result = [1] * length

for i in range(1,length):
  result[i] = result[i-1] * nums[i-1]

R = 1

for i in range(length-1,-1,-1):
  result[i] = result[i] * R
  R = R * nums[i]



print(result)