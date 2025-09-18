nums = [2,1,1,0,4]
max_reach = 0

flag = True
for i in range(len(nums)):
  if i > max_reach:
    flag = False
    break

  max_reach = max(max_reach,i+nums[i])
  if max_reach >= len(nums)-1:
    flag =True
    break
print(flag)