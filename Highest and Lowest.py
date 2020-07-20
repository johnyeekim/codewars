# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# 
# Example:
# 
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes:
# 
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


def high_and_low(numbers):
    num_str_list = numbers.split()

    num_int_list = []


    for num in num_str_list:
        num_int_list.append(int(num))
        
    max_num = str(max(num_int_list))
    min_num = str(min(num_int_list))
    numbers = max_num + " " + min_num
    return numbers
