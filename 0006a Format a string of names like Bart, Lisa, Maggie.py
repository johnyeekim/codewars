##Given: an array containing hashes of names
##
##Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
##
##Example:
##
##namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
### returns 'Bart, Lisa & Maggie'
##
##namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
### returns 'Bart & Lisa'
##
##namelist([ {'name': 'Bart'} ])
### returns 'Bart'
##
##namelist([])
### returns ''

def namelist(names):
  namesForString = [i['name'] for i in names]
  if len(namesForString) == 0:
    return ''
  elif len(namesForString) == 1:
    return namesForString[0]
  elif len(namesForString) == 2:
    return ' & '.join(namesForString)
  else:
    len(namesForString) > 2
    return ', '.join(namesForString[0:-1]) + ' & ' + ''.join(namesForString[-1])
