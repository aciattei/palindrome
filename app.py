word = input()

splitWord = word.split()

def inverter (splitWord):
  return splitWord[::-1]

invertedWord = inverter(word)

if invertedWord == word:
  print("The word " + word + " is a palindrome")

else: 
  print("The word " + word + " is not a palindrome")