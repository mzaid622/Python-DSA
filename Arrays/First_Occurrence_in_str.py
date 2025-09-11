haystack = "sabutsad"
needle = "sad"

length = len(haystack)
length2 = len(needle)
index = True
answer = -1
result = ""
for i in range(length):
  for j in range(length2):
    if haystack[i+j] == needle[j]:
      index = True
    else:
      index = False
      break
  if index == True:
    answer = i
    break
      

    

print(answer)
    
