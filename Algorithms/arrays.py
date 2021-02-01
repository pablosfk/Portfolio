def kadane(sequence):
    best_inf = []
    best_sup = []
    best_sum = sequence[:]
    # We calculate the acumulative sums array
    for i, current_value in enumerate(sequence):
        if i > 0:
            best_sum[i] = best_sum[i - 1] + current_value
            if best_sum[i] < 0:
                best_sum[i] = 0
    best_sum_max = max(best_sum)
    # We search the final index of heach sequence of maximun subarray sum
    while True:
        try:
            loc = best_sum.index(best_sum_max)
        except ValueError:
            break
        else:
            best_sup.append(loc)
            best_sum[loc] = 0
    # Now we must locate the start of each stretch
    for i, j in enumerate(best_sup):
        aux = best_sum_max
        while True:
            aux -= sequence[j]
            if aux == 0:
                best_inf.append(j)
                break
            else:
                j -= 1
    return best_inf, best_sup


'''
values = [-2, 1, -3, 4, -1, 2, 1, -5, 3, -3, 5] #[4, -1, 2, 1] y [4, -1, 2, 1, -5, 3, -3, 5]
#          0  1   2  3   4  5  6   7  8   9 10     from 3 to 6     from 3 to 10
print(kadane(values))
'''


def floyd(sequence):
    rabbit = 0
    turtle = 0
    length = len(sequence)
    while True:
        rabbit = sequence[rabbit]
        turtle = sequence[turtle]
        rabbit = sequence[rabbit]
        if rabbit == turtle:
            break
    rabbit = 0
    while True:
        rabbit = sequence[rabbit]
        turtle = sequence[turtle]
        if rabbit == turtle:
            break
    return rabbit


'''
seq = [6, 3, 9, 5, 1, 7, 2, 8, 4, 6]
print(floyd(seq))
'''


def kmp(sequence, pattern):
    # Prefix and suffix pattern search
    pattern_suffix = [0 for col in range(len(pattern))]
    j = 0
    for i, suf in enumerate(pattern):
        if i > 0 and pattern[j] == suf:
            pattern_suffix[i] = pattern_suffix[i - 1] + 1
            j += 1
        elif i > 0 and pattern[j] != suf:
            j = 0
    print(pattern_suffix)
    #Now we trhough the sequence looking for the pattern
    j = 0
    for i, value in enumerate(sequence):
        print(f'Tengo el valor {value} en la posición {i} y tengo que ver si es igual a {pattern[j]} de la posición {j} de pattern')
        if pattern[j] == value:
            j += 1
        elif pattern[j] != value:
            if j > 0:
                j = pattern_suffix[j-1]
                if pattern[j] == value:
                    j += 1
            elif j == 0 and pattern[j] == value:
                j += 1
        print(f'J quedó como {j}')
        if j == len(pattern):
            seq_ini = i - (j-1)
            seq_end = i
            break

    return seq_ini, seq_end

'''
A = 'A'
B = 'B'
C = 'C'
X = 'X'
seq = [A, A, B, A, A, C, C, X, A, A, B, X, A, A, B, A, C, A, A, B, A, A, C, A, A, B, C, A, X]
pattern = [A, A, B, A, A, C, A, A, B, C]
print(kmp(seq, pattern)) # [17, 26]
'''

