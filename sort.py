import math


def insertion(list):
    for i in range(len(list)):
        if i>0: #It does not work with the first number, we need at least 2 to can compare them
            if list[i]<list[i-1]: #Chek if the current number is less than the left one.
                aux = list[i]
                j=i
                while j != 0:
                    j -= 1
                    list[j+1] = list[j]
                    list[j] = aux
                    if list[j] > list[j - 1]:
                        break
    return list


'''
lista = [39, 83, 37, 18, -12, 73, 52, 1, 26, 76, 67, 20, 10, -3, 62, 28, 82, 91, 81, -58, 50, 72, 89, 29, 1]
lista1 = ['boca', 'carreta', 'jalea', 'altura', 'zorra', 'corral', 'batata']
print(insertion(lista))
print(insertion(lista1))
'''


def selection(list):
    length = len(list)
    for i in range(length):
        aux = list[i]
        j_aux = i
        for j in range(i, length):
            print(j)
            if list[j] < aux:
                aux = list[j]
                j_aux = j
        if list[j_aux] != list[i]:
            list[j_aux] = list[i]
            list[i] = aux
    return(list)


'''
lista = [39, 83, 37, 18, -12, 73, 52, 1, 26, 76, 67, 20, 10, -3, 62, 28, 82, 91, 81, -58, 50, 72, 89, 29, 1]
lista1 = ['boca', 'carreta', 'jalea', 'altura', 'zorra', 'corral', 'batata']
print(selection(lista))
print(selection(lista1))
'''


def heap(list):
    list_out = []
    while 1:
        length = len(list)
        rang = range(1, length)
        ready = True
        for i in rang:
            if 2*i-1 < length and list[2*i-1] > list[i-1]: #if the length is enough and son bigger than father
                aux = list[i-1]
                list[i-1] = list[2*i-1]
                list[2*i-1] = aux
                ready = False
            elif 2*i < length and list[2*i] > list[i-1]:
                aux = list[i-1]
                list[i-1] = list[2*i]
                list[2*i] = aux
                ready = False
        if ready:
            list_out.append(list[0])
            list.pop(0)
        if not list:
            list_out.reverse()
            break
    return list_out


'''
lista = [39, 83, 37, 18, -12, 73, 52, 1, 26, 76, 67, 20, 10, -3, 62, 28, 82, 91, 81, -58, 50, 72, 89, 29, 1]
lista1 = ['boca', 'carreta', 'jalea', 'altura', 'zorra', 'corral', 'batata']
print(heap(lista))
print(heap(lista1))
'''


def merge(list):
    divisions = [len(list)]
    if divisions[0] == 2 and list[0] > list[1]:
            list.reverse()
    else:
        levels = int(math.log2(len(list)))
        #Generating the subdivisions blocks
        while 1:
            for i in range(len(divisions)):
                if divisions[i] > 2:
                    divisions.insert(i, divisions[i]//2)
                    divisions[i+1] = divisions[i+1] - divisions[i]
            aux = 0
            for i in divisions:
                if i > 2:
                    aux += 1
            if aux == 0:
                break
        #print(divisions)

        #Then sort the list
        for i in range(levels): #Here we divide all work into merge levels
            for j in range(len(divisions)//2): #Here we through the whole level by pairs
                if divisions[j] <= divisions[j+1]:
                    sum = 0 #This variable will tell us the point we are in the list
                    for k in range(j):
                        sum += divisions[k] #Here we calculate the current position
                    list_aux = [list[sum+divisions[j]]] #We take the first value of the second block and put it first in auxiliary list
                    list.pop(sum+divisions[j]) #We pop it
                    l = divisions[j] #Number of values in block 1.
                    m = divisions[j+1]-1 #Number of values in block 2.
                    while l != 0 and m != 0:
                        if m == 0 or list[sum] <= list[sum+l]: #We study if first value from first block is less than first value of second block
                            for n in range(len(list_aux)): #The we study where it must be put in the auxiliary vector
                                if list[sum] <= list_aux[n]:
                                    list_aux.insert(n, list[sum])
                                    break
                                elif list[sum] > list_aux[len(list_aux)-1]:
                                    list_aux.append(list[sum])
                            list.pop(sum)
                            l -= 1
                        elif l == 0 or list[sum] >= list[sum+l]:
                            for n in range(len(list_aux)): #The we study where it must be put in the auxiliary vector
                                if list[sum+l] <= list_aux[n]:
                                    list_aux.insert(n, list[sum+l])
                                    break
                                elif list[sum+l] > list_aux[len(list_aux) - 1]:
                                    list_aux.append(list[sum+l])
                            list.pop(sum+l)
                            m -= 1
                    list_aux.reverse()
                    for o in list_aux: #here we insert the ordered values in auxiliary list into the real list
                        list.insert(sum, o)
                    divisions[j] = divisions[j] + divisions[j+1]
                    divisions.pop(j+1)
            #print(list)
    return list


'''
lista = [39, 83, 37, 18, -12, 73, 52, 1, 26, 76, 67, 20, 10, -3, 62, 28, 82, 91, 81, -58, 50, 72, 89, 29, 1]
lista1 = ['boca', 'carreta', 'jalea', 'altura', 'zorra', 'corral', 'batata']
print(merge(lista))
print(merge(lista1))
'''


def quick(list):
    def sort(list,lim_inf,lim_sup):
        if lim_inf != lim_sup:
            pivot = (lim_sup + lim_inf)//2
            pos = lim_inf
            lim_sup_aux = lim_sup
            pivot_quantity = 1
            while pos != lim_sup_aux+1:     # Through the whole list between lim_inf and lim_sup
                if pos < pivot and list[pos] > list[pivot]:
                    list.insert(lim_sup_aux+1, list[pos])  # Put the value at the end of the entered list
                    list.pop(pos)   # Eliminate the value
                    pos -= 1    # Correction of the position, due to the eliminated value we must stay in that place.
                    lim_sup_aux -= 1    # Correction of the end of the stretch, because we moved something to the end,
                    # we do not need to revisit it again
                    pivot -= 1     # Due to the eliminated value at left of pivot, we must move it
                elif pos > pivot and list[pos] < list[pivot]:
                    list.insert(lim_inf, list[pos])  # Put the value at the start of the entered list
                    list.pop(pos+1)   # Eliminate the value
                    pivot += 1     # Due to the inserted value at left of pivot, we must move it
                elif list[pos] == list[pivot] and pos != pivot:
                    pivot_quantity += 1
                    if pos < pivot:
                        list.insert(pivot, list[pos])
                        list.pop(pos)  # Eliminate the value
                        pos -= 1  # Correction of the position, due to the eliminated value we must stay in that place.
                        pivot -= 1  # Due to the eliminated value at left of pivot, we must move it
                    if pos > pivot:
                        list.insert(pivot, list[pos])
                        list.pop(pos + 1)  # Eliminate the value
                pos += 1
            if pivot > lim_inf:
                lim_inf1 = lim_inf
                lim_sup1 = pivot - 1
                sort(list, lim_inf1, lim_sup1)
            if pivot < lim_sup:
                lim_inf2 = pivot + pivot_quantity
                lim_sup2 = lim_sup
                sort(list, lim_inf2, lim_sup2)

    lim_inf = 0
    lim_sup = len(list)-1
    sort(list, lim_inf, lim_sup)
    return list


'''
lista = [39, 83, 37, 18, -12, 73, 52, 1, 26, 76, 67, 20, 10, -3, 62, 28, 82, 91, 81, -58, 50, 72, 89, 29, 1]
lista1 = ['boca', 'carreta', 'jalea', 'altura', 'zorra', 'corral', 'batata']
print(quick(lista))
print(quick(lista1))
'''


def counting(list):
    aux = []
    list_aux = []
    for i in range(max(list)+1):
        aux.append(0)
    for i in range(len(list)):
        list_aux.append(0)
    for i in list:
        aux[i] += 1
    temp = aux[0]
    for i in range(len(aux)-1):
        aux[i+1] += temp
        temp = aux[i+1]
    for i in list:
        list_aux[aux[i]-1] = i
        aux[i] -= 1

    return list_aux

'''
list = [1, 3, 8, 1, 2, 4, 5, 2, 1, 9, 1,  2,  0, 0]
print(counting(list))
'''