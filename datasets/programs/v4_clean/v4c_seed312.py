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
arr2[7] = 20
arr[2] *= 21
arr[2] *= 17
arr[5] = 21
arr[1] += 25
arr[3] += 8
"""


arr = [21, 5, 22, 13, 2, 24, 5, 11, 8, 7]
arr2 = arr[:]


arr[8] *= 2
arr[5] += 4
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 5
    else:
        arr[i] -= 2
arr[2] += 4
bump_if(arr, 7, 11, 5)
arr[1] -= 9
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 4
    else:
        arr[i] -= 1
arr[9] -= 2
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 2
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 1
arr[3] += 4
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 4
    else:
        arr[i] -= 2
arr[7] *= 2
arr[9], arr[8] = arr[8], arr[9]
arr.reverse()
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 5
arr[8:9] = sorted(arr[8:9])
arr[8:9] = sorted(arr[8:9])
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 5
bump_if(arr, 3, 15, 5)

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
