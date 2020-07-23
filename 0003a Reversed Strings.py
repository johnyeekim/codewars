##Complete the solution so that it reverses the string passed into it.
##
##'world'  =>  'dlrow'

def solution(string):
    list1 = list(string)
    list1.reverse()
    return ''.join(list1)
