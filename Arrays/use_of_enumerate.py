nums = [3,5,4,6]
target = 7
num_to_index = {}

for i,num in enumerate(nums):
  complement = target - num
  if complement in num_to_index:
    print(num_to_index[complement],i)
    break
  num_to_index[num] = i
  