# Brute Force
# nums = [1,2,3,4,5,6,7]
# k = 3

# # for i in range(k):
# #   last = nums[-1]
# #   for j in range(len(nums)-1,0,-1):
# #     nums[j] = nums[j-1]
# #   nums[0] = last
# #   print(nums)


# Two Pointer


def rever(nums, start, end):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(nums)
nums.reverse()
k = k % n

rever(nums, 0, k - 1)
rever(nums,k,n-1)

print(nums)
