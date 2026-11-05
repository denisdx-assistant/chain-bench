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
arr[4], arr[1] = arr[1], arr[4]
arr[8] += 7
arr2[8] = 3
arr[4] += 52
arr[7] *= 40
arr2[0] = 56
"""


arr = [13, 21, 26, 30, 16, 18, 15, 21, 8, 22]
arr2 = arr[:]


arr.reverse()
arr[5] += 1
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 3
arr[1] += 8
bump_if(arr, 6, 5, 6)
bump_if(arr, 4, 7, 5)
arr[3] -= 9
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 4
    else:
        arr[i] -= 4
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 5
bump_if(arr, 0, 14, 3)
arr.reverse()
arr[9], arr[6] = arr[6], arr[9]
arr[6:7] = sorted(arr[6:7])
arr[2] -= 6
arr[7] += 8
arr[3], arr[6] = arr[6], arr[3]
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 1
arr[8:9] = sorted(arr[8:9])
arr[6:9] = sorted(arr[6:9])
bump_if(arr, 5, 12, 3)

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
