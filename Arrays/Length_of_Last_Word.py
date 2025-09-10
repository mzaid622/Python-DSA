# s = "Hello World"
# new_s=s.split()

# last_word = new_s[-1]

# print(last_word)

# 2nd Approach

str = "fly me   to   the moon  "
length=len(str)
count = 0
for i in range(length-1,-1,-1):
  if (str[i] == " "):
    if count > 0:
      break
  else:
    count +=1
print(count)

