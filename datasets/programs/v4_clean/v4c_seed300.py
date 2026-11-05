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
arr[9], arr[2] = arr[2], arr[9]
arr[6] = 24
arr[2], arr[3] = arr[3], arr[2]
arr[9] = 50
arr[0], arr[1] = arr[1], arr[0]
arr[8] *= 33
"""


arr = [20, 12, 12, 1, 16, 12, 17, 27, 29, 14]
arr2 = arr[:]


arr[5] += 2
bump_if(arr, 1, 11, 4)
arr[0] -= 3
arr.reverse()
arr[4], arr[3] = arr[3], arr[4]
bump_all(arr, 4)
arr[4] += 9
arr[6] -= 6
bump_if(arr, 6, 7, 1)
arr[6] += 1
arr[5] += 9
arr[5:6] = sorted(arr[5:6])
arr[3] += 9
arr[8] += 7
bump_all(arr, 5)
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 4
arr[1], arr[3] = arr[3], arr[1]
arr[1] += 8
bump_if(arr, 4, 22, 4)
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 5

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
