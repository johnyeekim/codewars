##Welcome.
##
##In this kata you are required to, given a string, replace every letter with its position in the alphabet.
##
##If anything in the text isn't a letter, ignore it and don't return it.
##
##"a" = 1, "b" = 2, etc.

##alphabet_position("The sunset sets at twelve o' clock.")
##Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

def alphabet_position(text):
  position = list(range(1,27))
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  dict1 = dict(zip(alphabet, position))
  letterList = []
  positionList = []
  
  if text == "": return ""

  for i in text.lower():
    if i.isalpha():
      letterList += [' '.join(i)]
      positionList = [str(dict1[x]) for x in letterList]
      
  return ' '.join(positionList)


      
