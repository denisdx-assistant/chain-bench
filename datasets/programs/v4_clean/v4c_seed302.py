"""Тест 2 v3: исполнить программу и назвать сумму массива arr."""

def bump_all(a, v):
    for i in range(0, len(a), 2):
        a[i] += v

def bump_if(a, i, limit, v):
    if a[i] > limit:
        a[i] -= v
    else:
        a[i] += v

MANUAL = """
arr2[3] = 50
arr2[5] = 43
arr[0], arr[3] = arr[3], arr[0]
arr[8] += 44
arr[1], arr[5] = arr[5], arr[1]
arr2[7] = 35
"""


arr = [18, 18, 28, 18, 14, 16, 7, 27, 2, 13]
arr2 = arr[:]


bump_all(arr, 3)
bump_if(arr, 1, 14, 2)
arr[3] -= 9
arr.reverse()
arr[3], arr[0] = arr[0], arr[3]
arr[7], arr[6] = arr[6], arr[7]
arr.reverse()
arr[0] += 4
arr[2:4] = sorted(arr[2:4])
arr[3] += 9
arr[7], arr[8] = arr[8], arr[7]
arr[0] += 8
arr[6], arr[4] = arr[4], arr[6]
arr[9] += 7
bump_if(arr, 1, 13, 4)
arr[2] -= 4
arr[5] *= 2
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 4
    else:
        arr[i] -= 1
bump_all(arr, 5)
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 4

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
