strs = ["flower", "flow", "flight"]

length = len(strs[0])
result = ""
for i in range(length):
  char = strs[0][i]
  for j in range(1,len(strs)):
    if (char != strs[j][i]):
      print(result)
      exit()
  result += char
  


      
print(result)
    
