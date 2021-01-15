def insertion(list):
    aux = 0
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
lista = [39, 83, 37, 18, 73, 52, 1, 26, 76, 67, 20, 10, 62, 28, 82, 91, 81, 50, 72, 89, 29, 1]
lista1 = ['boca', 'carreta', 'jalea', 'altura', 'zorra', 'corral', 'batata']
print(insertion(lista1))
'''


