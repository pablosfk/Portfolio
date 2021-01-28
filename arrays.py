def kadane(sequence):
  best_inf = []
  best_sup = []
  best_sum = sequence[:]
  #We calculate the acumulative sums array
  for i, current_value in enumerate(sequence):
    if i > 0:
      best_sum[i] = best_sum[i - 1] + current_value
      if best_sum[i] < 0:
        best_sum[i] = 0
  best_sum_max = max(best_sum)
  #We search the final index of heach sequence of maximun subarray sum
  while True:
    try:
      loc = best_sum.index(best_sum_max)
    except ValueError:
      break
    else:
      best_sup.append(loc)
      best_sum[loc] = 0
  #Now we must locate the start of each stretch
  for i,j in enumerate(best_sup):
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

