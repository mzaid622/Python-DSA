roman_mapping = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}

string = input("Enter number that you want to convert into roman: ")

number = int(string)
result = ""

while number > 0:
  for value,symbol in roman_mapping.items():
    if number >= value:
      number -= value
      result = result + roman_mapping[value]
      break
  

print(result)


  

