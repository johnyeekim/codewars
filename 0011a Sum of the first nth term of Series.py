##Your task is to write a function which returns the sum of following series upto nth term(parameter).
##
##Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
##
##Rules:
##You need to round the answer to 2 decimal places and return it as String.
##
##If the given value is 0 then it should return 0.00
##
##You will only be given Natural Numbers as arguments.
##
##Examples:
##SeriesSum(1) => 1 = "1.00"
##SeriesSum(2) => 1 + 1/4 = "1.25"
##SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"

def series_sum(n):
  n_series = 0

  if n == 0: return '0.00'
  if n == 1: return '1.00'
  if n == 2: return '1.25'
  for i in range(3,n+1):
    n_series += 1/(4+((i-2)*3))
  return format((1 + 1/4 + n_series), '.2f')
