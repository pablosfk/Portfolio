def linSearch(list, value):
  ''' This function will search a value in a list using linear search method.'''
  #If receive True, the second number indicates the position of the found value into the list

  found = False
  pos = 0
  for i in range(len(list)):
    if list[i]==value:
      found = True
      pos = i
      break

  return found, pos

a = [1, 15, 2, 75, 5, 'ab', 23, 17, 'a', 9, 152, 247, 3, 31, 29]
print(linSearch(a,3))
print(linSearch(a,32))
print(linSearch(a,'a'))
print(linSearch(a,'b'))