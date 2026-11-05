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
arr2[2] = 31
arr[1], arr[4] = arr[4], arr[1]
arr[0], arr[9] = arr[9], arr[0]
arr[6] = 32
arr[0] *= 44
arr2[4] = 15
"""


arr = [2, 8, 24, 7, 3, 19, 20, 9, 19, 17]
arr2 = arr[:]


arr[2] += 4
arr[1:4] = sorted(arr[1:4])
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 3
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 4
arr[8] += 2
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 4
arr[9], arr[3] = arr[3], arr[9]
arr.reverse()
arr[5], arr[2] = arr[2], arr[5]
arr[3] += 9
bump_all(arr, 1)
arr[4], arr[3] = arr[3], arr[4]
arr[2] *= 2
arr[8], arr[2] = arr[2], arr[8]
arr[9:10] = sorted(arr[9:10])
arr[6], arr[2] = arr[2], arr[6]
arr[7] += 9
arr[5] *= 2
arr[7] *= 2
arr[4], arr[6] = arr[6], arr[4]

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
