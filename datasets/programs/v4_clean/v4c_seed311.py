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
arr[0], arr[8] = arr[8], arr[0]
arr[5] += 7
arr[9] += 47
arr[1] *= 15
arr[4], arr[5] = arr[5], arr[4]
arr2[7] = 17
"""


arr = [27, 9, 9, 24, 3, 14, 16, 29, 5, 9]
arr2 = arr[:]


bump_if(arr, 0, 23, 5)
bump_all(arr, 2)
bump_if(arr, 0, 14, 6)
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 5
bump_if(arr, 8, 25, 5)
arr[1], arr[5] = arr[5], arr[1]
bump_if(arr, 8, 22, 3)
arr[2] *= 2
arr[1] += 9
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 5
bump_all(arr, 5)
bump_all(arr, 3)
arr[9] += 6
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 3
bump_all(arr, 3)
arr[0] += 6
arr[0] *= 2
arr[0] *= 2
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 2
arr[6] += 1

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
