def qsort(arr, i, j):
   if i == j:
      return
   i1 = i
   j1 = j
   N = arr[i]
   k = i1
   while k != j1:
      if arr[k] == N:
         k += 1
      elif arr[k] < N:
         arr[i1], arr[k] = arr[k], arr[i1]
         i1 += 1
         k += 1
      elif arr[k] > N:
         j1 -= 1
         arr[j1], arr[k] = arr[k], arr[j1]
   qsort(arr, i, i1)
   qsort(arr, j1, j)

n = int(input())
a = list(map(int, input().split()))
qsort(a, 0, len(a))
print(' '.join(map(str, a)))

