citations = [1]

length = len(citations)
count = 0
ans = 0
for h in range(1, length + 1):
    for i in range(length):
        if h <= citations[i]:
            count += 1
    if count >= h:
        ans = h
    else:
        break
    count = 0

print(ans)
