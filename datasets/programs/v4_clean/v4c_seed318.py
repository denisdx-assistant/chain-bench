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
arr[6] *= 23
arr[6] += 1
arr[6] = 45
arr2[7] = 31
arr2[1] = 33
arr[3] *= 5
"""


arr = [23, 21, 2, 15, 13, 25, 14, 6, 20, 27]
arr2 = arr[:]


bump_all(arr, 2)
arr.reverse()
arr[2], arr[5] = arr[5], arr[2]
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 3
arr[1] -= 9
arr[0] += 5
bump_all(arr, 1)
arr[6:7] = sorted(arr[6:7])
arr.reverse()
bump_all(arr, 1)
arr.reverse()
arr[4] *= 2
bump_all(arr, 1)
arr.reverse()
arr[4] += 1
arr[0], arr[5] = arr[5], arr[0]
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 1
bump_if(arr, 4, 6, 3)
arr[7], arr[2] = arr[2], arr[7]
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 4

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
