s = "jar" 
t = "jam"

length_s = len(s)
length_t = len(t)
flag = False

if length_s != length_t:
  flag = True
else:
  s1 = ''.join(sorted(s))
  t1 = ''.join(sorted(t))
  for i in range(length_s):
    if s1[i] != t1[i]:
      flag = True
      break

if(flag):
  print("Not Valid Anagram")
else:
  print("Valid Anagram")


