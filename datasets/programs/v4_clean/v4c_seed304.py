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
arr[3] *= 48
arr[0] += 19
arr[1] *= 25
arr[2] += 30
arr[5], arr[9] = arr[9], arr[5]
arr[9] *= 30
"""


arr = [5, 7, 14, 17, 28, 15, 2, 8, 26, 22]
arr2 = arr[:]


arr[2] -= 6
arr[7] *= 2
arr[3] -= 3
arr[6] += 2
arr[4], arr[7] = arr[7], arr[4]
bump_if(arr, 0, 16, 3)
arr[2] += 3
arr[1] += 4
bump_all(arr, 2)
for i in range(0, 10, 2):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 1
arr[6] -= 7
arr[7], arr[9] = arr[9], arr[7]
arr[8:9] = sorted(arr[8:9])
arr[1], arr[3] = arr[3], arr[1]
arr[9], arr[6] = arr[6], arr[9]
bump_all(arr, 1)
arr[2], arr[4] = arr[4], arr[2]
bump_all(arr, 3)
arr[3], arr[1] = arr[1], arr[3]
bump_if(arr, 3, 6, 1)

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
