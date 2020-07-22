##Check to see if a string has the same amount of 'x's and 'o's. The method mus>
##
##Examples input/output:
##
##XO("ooxx") => true
##XO("xooxx") => false
##XO("ooxXm") => true
##XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
##XO("zzoo") => false

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
