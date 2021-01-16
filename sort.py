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
    #Los hijos son list(i*2) y list(i*2+1) siendo i los padres, y padres son todos aquellos donde se cumple esa
    #ecuación sin sobrepasar el largo de la lista: list(i*2) < len(list)-1 y list(i*2+1) < len(list)-1
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