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
arr[5], arr[5] = arr[5], arr[5]
arr2[3] = 38
arr[2] *= 14
arr[9] += 24
arr[6], arr[1] = arr[1], arr[6]
arr[5] *= 41
"""


arr = [18, 3, 7, 22, 9, 6, 10, 19, 29, 28]
arr2 = arr[:]


arr[1] *= 2
arr[1], arr[7] = arr[7], arr[1]
bump_if(arr, 7, 23, 6)
arr[2] -= 5
bump_all(arr, 4)
arr[2], arr[1] = arr[1], arr[2]
arr[5:6] = sorted(arr[5:6])
arr.reverse()
arr[2], arr[7] = arr[7], arr[2]
bump_all(arr, 4)
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 5
    else:
        arr[i] -= 3
arr[0] -= 6
arr[7] += 5
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 4
bump_if(arr, 9, 8, 3)
arr[7] -= 4
arr[0] += 1
arr[1], arr[8] = arr[8], arr[1]
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 4
    else:
        arr[i] -= 4
bump_all(arr, 3)

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
