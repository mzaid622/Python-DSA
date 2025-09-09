prices = [7,1,5,3,6,4]

profit = 0
length = len(prices)
for i in range(length):
  for j in range(length):
    if (j > i):
      profit = max(profit,prices[j] - prices[i])

print(profit)