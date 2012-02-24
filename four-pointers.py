I = 4

array = []
mmm = []
for i in range(I):
    mmm.append(int(input()))
    array.append(list(map(int, input().split())))

best = [0] * I
curr = [0] * I

def values(arr):
    result = []
    for i in range(I):
        index = arr[i]
        value = array[i][index]
        result.append(value)
    return result

def score(arr):
    vv = values(arr)
    return max(vv) - min(vv)

def ok():
    for i in range(I):
        if not curr[i] < mmm[i]:
            return False
    return True

while ok():
    vv = values(curr)
    min_value = min(vv)
    min_index = vv.index(min_value)
    curr[min_index] += 1
    if curr[min_index] < mmm[min_index] and score(curr) < score(best):
        best = list(curr)
print(' '.join(map(str, values(best))))

