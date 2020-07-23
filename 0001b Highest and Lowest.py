#Description:
#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#
#Example:
#
#high_and_low("1 2 3 4 5")  # return "5 1"
#high_and_low("1 2 -3 4 5") # return "5 -3"
#high_and_low("1 9 3 4 -5") # return "9 -5"
#Notes:
#
#All numbers are valid Int32, no need to validate them.
#There will always be at least one number in the input string.
#Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers): #z.
    
    #List comprehension: A concise way of creating lists. Lists that generate themselves with an internal for loop / if statement.
    
    #Python documentation: “A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.”
    
    nn = [int(s) for s in numbers.split(" ")]

    
    return "%i %i" % (max(nn),min(nn))