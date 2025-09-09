prices = [7,1,5,3,6,4]

# This is brute Force
# profit = 0
# length = len(prices)
# for i in range(length):
#   for j in range(length):
#     if (j > i):
#       profit = max(profit,prices[j] - prices[i])

# print(profit)


max_price = 0
min_price = float('inf')

for i in prices:
  min_price = min(min_price,i)
  max_price = max(max_price,i-min_price)
print(max_price)