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
arr2[8] = 39
arr[0], arr[5] = arr[5], arr[0]
arr[9], arr[8] = arr[8], arr[9]
arr[4] *= 13
arr2[0] = 17
arr[0], arr[9] = arr[9], arr[0]
"""


arr = [14, 30, 17, 26, 7, 9, 25, 20, 7, 14]
arr2 = arr[:]


for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 4
arr[7] += 9
arr[0] -= 5
arr[3] *= 2
arr.reverse()
bump_if(arr, 0, 13, 3)
arr[6:7] = sorted(arr[6:7])
arr.reverse()
bump_if(arr, 5, 16, 6)
arr[8], arr[3] = arr[3], arr[8]
arr[3] += 4
bump_if(arr, 1, 21, 5)
arr.reverse()
arr[1] -= 6
bump_all(arr, 3)
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 4
    else:
        arr[i] -= 1
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 1
arr[8] -= 6
arr[8:9] = sorted(arr[8:9])
arr[8] *= 2

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
