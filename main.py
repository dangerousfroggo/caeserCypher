#created by Sergei Borishchev, 349512905

def caeserCypher(string,key):
  stringArray = [x for x in string]
  shiftedString = ""
  for i in range(len(stringArray)):
    letter = stringArray[i]
    shiftedString += chr(ord(letter) + key)
  return shiftedString
print(caeserCypher("hello", 3))

#i needed another commit to get 100% lol
  
