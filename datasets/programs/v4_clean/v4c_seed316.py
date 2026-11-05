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
arr[3] += 49
arr[7] = 5
arr2[8] = 15
arr[2] = 54
arr[8] += 45
arr[7], arr[5] = arr[5], arr[7]
"""


arr = [1, 26, 28, 1, 26, 11, 29, 26, 1, 27]
arr2 = arr[:]


bump_all(arr, 2)
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 5
arr[8] -= 7
bump_all(arr, 4)
arr.reverse()
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 5
    else:
        arr[i] -= 1
bump_all(arr, 1)
arr[7], arr[1] = arr[1], arr[7]
arr[0] += 7
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 3
arr[4] *= 2
bump_if(arr, 6, 18, 3)
arr.reverse()
arr[6], arr[2] = arr[2], arr[6]
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 3
bump_if(arr, 6, 20, 4)
arr[0:10] = sorted(arr[0:10])
arr[4], arr[6] = arr[6], arr[4]
arr[6] += 7
arr.reverse()

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
