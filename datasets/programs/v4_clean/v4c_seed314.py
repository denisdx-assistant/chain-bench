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
arr[6] += 57
arr2[0] = 9
arr[3] = 16
arr[4], arr[0] = arr[0], arr[4]
arr[5] += 53
arr[8] *= 48
"""


arr = [7, 15, 4, 6, 1, 21, 21, 10, 8, 13]
arr2 = arr[:]


arr[5] += 9
arr.reverse()
arr[7] *= 2
arr[3] -= 9
bump_all(arr, 4)
bump_all(arr, 1)
bump_all(arr, 4)
bump_all(arr, 3)
arr.reverse()
arr[0] += 4
bump_if(arr, 9, 25, 3)
arr[0] += 2
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 1
arr[3] -= 1
arr[7] -= 5
arr[8], arr[5] = arr[5], arr[8]
arr[0] -= 7
arr[5] -= 2
bump_if(arr, 5, 12, 4)
arr[4:9] = sorted(arr[4:9])

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
