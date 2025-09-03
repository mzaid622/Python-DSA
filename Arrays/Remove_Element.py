nums = [3,2,2,3]
val = 3

i=0
j = 0 

for _ in range(len(nums)):
  if nums[i] != val:
    nums[j] = nums[i]
    j +=1
    i +=1
  elif nums[i] == val:
    i +=1

    
print(j)
print(nums)