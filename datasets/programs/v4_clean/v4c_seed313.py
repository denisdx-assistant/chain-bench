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
arr[5] = 2
arr[7] += 31
arr[6], arr[2] = arr[2], arr[6]
arr[1] += 1
arr[3], arr[8] = arr[8], arr[3]
arr[5] += 3
"""


arr = [19, 6, 22, 14, 16, 28, 1, 7, 27, 5]
arr2 = arr[:]


arr[7] += 1
arr[4:8] = sorted(arr[4:8])
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 4
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 4
bump_if(arr, 0, 10, 5)
arr[9] *= 2
arr[2] *= 2
bump_if(arr, 7, 21, 6)
arr[0], arr[0] = arr[0], arr[0]
arr[0] += 9
bump_all(arr, 4)
arr[7:8] = sorted(arr[7:8])
arr[8:9] = sorted(arr[8:9])
arr[8:10] = sorted(arr[8:10])
arr[4:6] = sorted(arr[4:6])
arr[6:7] = sorted(arr[6:7])
arr[0] += 3
arr[7:8] = sorted(arr[7:8])
bump_if(arr, 4, 18, 4)
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 1

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
