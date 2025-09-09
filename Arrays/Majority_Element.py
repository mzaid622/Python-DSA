# This is solving Hash Map
# nums = [2,2,1,1,1,2,2]
# dict = {
# }
# for num in nums:
#   if num in dict:
#     dict[num] += 1
#   else:
#     dict[num] =1
# answer = 0
# for key,value in dict.items():
#   if (len(nums)//2 < value):
#     answer = key
#     break
# print(answer)    


# 2nd Approach Boyer-Moore Voting Algo

nums = [2,2,1,1,1,2,2]


count = 0

for num in nums:
  if count == 0:
    candiate = num
    count = 1
  elif candiate == num:
    count +=1
  else:
    count -=1
print(candiate)