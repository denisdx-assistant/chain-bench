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
arr2[0] = 54
arr[6] *= 35
arr[1] += 40
arr[9] = 48
arr[5] = 17
arr[3] = 11
"""


arr = [3, 10, 1, 5, 7, 29, 29, 8, 7, 8]
arr2 = arr[:]


arr[1] += 7
bump_if(arr, 6, 19, 5)
bump_if(arr, 6, 16, 4)
arr[0] += 3
bump_all(arr, 4)
arr[4], arr[1] = arr[1], arr[4]
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 5
    else:
        arr[i] -= 5
arr[0:7] = sorted(arr[0:7])
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 5
    else:
        arr[i] -= 3
arr[5] -= 1
bump_all(arr, 2)
arr[1], arr[2] = arr[2], arr[1]
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 2
arr[5] -= 5
arr[4], arr[0] = arr[0], arr[4]
arr[1], arr[8] = arr[8], arr[1]
arr[2:8] = sorted(arr[2:8])
arr[5], arr[3] = arr[3], arr[5]
bump_if(arr, 9, 20, 3)
arr[1], arr[0] = arr[0], arr[1]

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
