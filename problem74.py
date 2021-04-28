def makeRoman(num):
      places_array = [0,0,0,0]
  index = 0
  roman = ""
  while num >= 1:
    places_array[index] = num % 10 
    num = num//10
    index += 1 
  print(places_array[0])
  return makeRoman2(places_array[3]*1000) + makeRoman2(places_array[2]*100) + makeRoman2(places_array[1]*10) + makeRoman2(places_array[0])

def makeRoman2(num):
  if num == 4:
    return "IV"
  elif num == 9:
    return "IX"
  elif num == 40:
    return "XL"
  elif num == 90:
    return "XC"
  elif num == 400:
    return "CD"
  elif num == 900:
    return "CM"
  else:
    count_M = 0
    count_D = 0
    count_C = 0
    count_L = 0
    count_X = 0
    count_V = 0
    count_I = 0
    while num >=5 :
      if num / 1000 >= 1:
        count_M += 1
        num -= 1000
      elif num / 500 >= 1:
        count_D += 1
        num -= 500
      elif num / 100 >= 1:
        count_C += 1
        num -= 100
      elif num / 50 >= 1:
        count_L += 1
        num -= 50
      elif num / 10 >= 1:
        count_X += 1
        num -= 10 
      elif num / 5 >= 1:
        count_V += 1
        num -= 5 
    if num >= 1:def makeRoman(num):
      places_array = [0,0,0,0]
  index = 0
  roman = ""
  while num >= 1:
    places_array[index] = num % 10 
    num = num//10
    index += 1 
  print(places_array[0])
  return makeRoman2(places_array[3]*1000) + makeRoman2(places_array[2]*100) + makeRoman2(places_array[1]*10) + makeRoman2(places_array[0])

def makeRoman2(num):
  if num == 4:
    return "IV"
  elif num == 9:
    return "IX"
  elif num == 40:
    return "XL"
  elif num == 90:
    return "XC"
  elif num == 400:
    return "CD"
  elif num == 900:
    return "CM"
  else:
    count_M = 0
    count_D = 0
    count_C = 0
    count_L = 0
    count_X = 0
    count_V = 0
    count_I = 0
    while num >=5 :
      if num / 1000 >= 1:
        count_M += 1
        num -= 1000
      elif num / 500 >= 1:
        count_D += 1
        num -= 500
      elif num / 100 >= 1:
        count_C += 1
        num -= 100
      elif num / 50 >= 1:
        count_L += 1
        num -= 50
      elif num / 10 >= 1:
        count_X += 1
        num -= 10 
      elif num / 5 >= 1:
        count_V += 1
        num -= 5 
    if num >= 1:
      count_I = num 
      # print("yo")
    print(count_L, count_V, count_I)  
    return "M"*count_M + "D"*count_D +"C"*count_C + "L"*count_L + "X"*count_X + "V"*count_V + "I"*count_I


input1 = 6
input2 = 4
input3 = 9
input4 = 58
input5 = 1994
print(makeRoman(input1))
# print(makeRoman(input2))
# print(makeRoman(input3))
# print(makeRoman(input4))
# print(makeRoman(input5))
# print("M"*2)


      count_I = num 
      # print("yo")
    print(count_L, count_V, count_I)  
    return "M"*count_M + "D"*count_D +"C"*count_C + "L"*count_L + "X"*count_X + "V"*count_V + "I"*count_I


input1 = 6
input2 = 4
input3 = 9
input4 = 58
input5 = 1994
print(makeRoman(input1))
# print(makeRoman(input2))
# print(makeRoman(input3))
# print(makeRoman(input4))
# print(makeRoman(input5))
# print("M"*2)

