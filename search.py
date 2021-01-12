def linSearch(list, value):
''' This function will search a value in a list
using linear search method.'''

  found = False
  pos = 0
  for i in range(len(list)):
    if list[i]==value:
      found = True
      pos = i
      break
      
return found, pos
