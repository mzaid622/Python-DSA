s = "the sky is blue"


# Approach 1

new_s=s.split()
length = len(new_s) -1
answer = ""
for i in range(length,-1,-1):
  answer += new_s[i]
  answer += " "
print(answer.strip())


# Approach 2
# i = len(s) - 1
# answer = []
# while i >= 0:
#     while i >= 0 and s[i] == " ":
#         i -= 1

#     if i < 0:
#         break

#     end = i
#     while i >= 0 and s[i] != " ":
#         i -= 1

#     start = i + 1

#     answer.append(s[start : end + 1])


# print(answer)
