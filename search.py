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

"""a = [1, 15, 2, 75, 5, 'ab', 23, 17, 'a', 9, 152, 247, 3, 31, 29]
print(linSearch(a,3))
print(linSearch(a,32))
print(linSearch(a,'a'))
print(linSearch(a,'b'))"""


def binSearch(list, value):
  ''' This function will search a value in a ordered list using bilinear search method.'''
  #If receive True, the second number indicates the position of the found value into the list
  found = False
  pos = 0
  pos_init = 0
  pos_end = len(list)-1
  pos_aux = 0
  while 1:
    pos_i = (pos_init + pos_end)//2
    if pos_i != pos_aux:
      if list[pos_i] == value:
        pos = pos_i
        found = True
        break
      elif value < list[pos_i]:
        pos_end = pos_i - 1
      else:
        pos_init = pos_i + 1
      pos_aux = pos_i
    else:
      break

  return found, pos

'''a = [1, 4, 9, 14, 25, 34, 45, 57, 61, 69, 72, 77, 83, 91, 129]

for i in a:
  print(binSearch(a,i))
print(binSearch(a,1520))'''