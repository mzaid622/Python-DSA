nums = [0,0,1,1,1,2,2,3,3,4]

fast = 0
slow = 0

for fast in range(1,len(nums)):
  if(nums[fast] != nums[slow]):
    nums[slow+1] = nums[fast]
    slow +=1

print(slow+1)
print(nums)