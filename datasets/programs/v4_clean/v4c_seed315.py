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
arr[4] += 44
arr[1] *= 2
arr[8] = 14
arr[1], arr[4] = arr[4], arr[1]
arr[6], arr[1] = arr[1], arr[6]
arr[0] *= 30
"""


arr = [14, 23, 14, 11, 1, 12, 19, 21, 2, 3]
arr2 = arr[:]


arr[5], arr[3] = arr[3], arr[5]
arr[3], arr[8] = arr[8], arr[3]
arr[3] += 5
arr[9] += 6
bump_all(arr, 3)
arr.reverse()
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 4
    else:
        arr[i] -= 5
arr[1] *= 2
bump_if(arr, 0, 18, 2)
arr[0] += 6
arr[4] += 7
arr[9] += 2
arr[0] += 6
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 1
bump_if(arr, 9, 13, 2)
bump_all(arr, 2)
bump_all(arr, 2)
arr[2] -= 3
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 1
arr[3] *= 2

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
