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
  ''' This function will search a value in a ordered list using binary search method.'''
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


def DFSearch(dict, start, end):
  ''' This function will find the route from START to END in a graph described by conections (tuples) in dictionary DICT'''
  ''' Dict = {'Node_A' : ('Node_B', 'Node_C'), 'Node_B': ('Node_A', 'Node_D', 'Node_E')....}'''
  # The function will return the route found from START to END.
  schedule = [] #stack
  route = []
  station = start.upper()
  expanded = [station]
  cameFrom = [station] #Here it loads the Expanded came from
  cameFromAux = [] #Here it loads the Schedule came from
  end = end.upper()
  found = False
  if station == end:
    print('Choose a different start and end of the route')
    route = 'None'
  else:
    while found==False:
      for i in dict[station]: #Expanding node
        if i.upper() == end:
          # We found the end-point
          route = [i.upper()]
          route.append(expanded[-1])
          while route[-1] != start.upper():
            route.append(cameFrom [expanded.index(route[-1])])
          found = True
          route.reverse()
          break #Finishing function
        elif expanded.count(i.upper()) == 0:  #Looking for if this station is not in the expanded list
          schedule.append(i.upper())
          cameFromAux.append(station)
      #Here we have the schedule loaded
      expanded.append(schedule[-1]) #Add to expanded the last added in schedule
      cameFrom.append(cameFromAux[-1])
      schedule.pop(-1) #Delete the last one in schedule
      cameFromAux.pop(-1) #Delete the last one in cameFrom
      station = expanded[-1]

  route = str(route)
  route = route.replace('[' , '')
  route = route.replace(']' , '')
  route = route.replace(',' , ' ->')
  return 'Route is: ' + route
'''
dict_1 = {'A':('T'), 'B': ('F'), 'C': ('N'), 'D':('Q'), 'E':('L'), 'F':('B','O'), 'G':('O', 'S'), 'H':('J')}
dict_2 = {'I':('R', 'S', 'T', 'N'), 'J':('N', 'T', 'L', 'H'), 'K':('Q'), 'L':('E', 'J'), 'M':('P', 'R', 'S')}
dict_3 = {'N':('R', 'I', 'J', 'C'), 'O':('F', 'T', 'G', 'Q'), 'P':('S', 'M'), 'Q':('K', 'S', 'O', 'D')}
dict_4 = {'R':('N', 'M', 'S', 'I'), 'S':('I', 'R', 'M', 'P', 'Q', 'G'), 'T':('J', 'O', 'I', 'A')}
dict = {**dict_1, **dict_2, **dict_3, **dict_4}

start = 'd'
end = 'e'
print(DFSearch(dict, start, end))
'''