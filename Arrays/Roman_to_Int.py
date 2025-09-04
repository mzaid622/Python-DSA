roman_mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

roman = input("Input Roman: ")
result = 0
for i in range(len(roman) -1):
  current = roman[i]
  next = roman[i+1]
  if roman_mapping[current] < roman_mapping[next]:
    result -= roman_mapping[current]
  else:
    result += roman_mapping[current]

new_value = roman[-1]
result += roman_mapping[new_value]
print(result)

    

  

