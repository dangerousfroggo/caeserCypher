#created by Sergei Borishchev, 349512905

def caeserCypher(string,key):
  stringArray = [x for x in string]
  shiftedString = ""
  for i in range(len(stringArray)):
    j = string[i]
    if ord(j) + key > 96 and ord(j) + key < 123:
      shiftedString += chr(ord(j) + key)
    elif ord(j) + key > 122:
      shiftedString += chr(ord(j) + key - 26)
    elif ord(j) + key < 97:
      shiftedString += chr(ord(j) + key + 26)
  return shiftedString
print(caeserCypher("cryptography", -15))

#i needed another commit to get 100% lol
  
