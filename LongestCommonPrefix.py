strs = ["flower", "flow", "flight"]

# length = len(strs[0])
# result = ""
# for i in range(length):
#   char = strs[0][i]
#   for j in range(1,len(strs)):
#     if (char != strs[j][i]):
#       print(result)
#       exit()
#   result += char
# print(result)
    
# 2nd Approach
new_list = sorted(strs)
min_length = min(len(new_list[0]),len(new_list[-1]))
result = ""
for i in range(min_length):
  if new_list[0][i] == new_list[-1][i]:
    result += new_list[0][i]
  else:
    break
print(result)