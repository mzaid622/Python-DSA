# Solving Problem in 0(n2)

# length = len(nums)
# flag = False

# for i in range(length):
#   for j in range(i+1,length):
#     if nums[i] == nums[j]:
#       flag = True
#       break

# if(flag):
#   print("Duplicate")
# else:
#   print("No Duplicate")
      
nums = [2,4,6,7,5]
seen = set()
flag = False

for i in range(len(nums)):
  if nums[i] in seen:
    flag = True
    break
  else:
    seen.add(nums[i])

if(flag):
  print("Duplicate")
else:
  print("No Duplicate")
  
