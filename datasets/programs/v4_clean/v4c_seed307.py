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
arr[6] = 38
arr[1] *= 44
arr2[4] = 59
arr[2] = 43
arr[8] += 12
arr2[2] = 5
"""


arr = [21, 17, 10, 25, 23, 10, 17, 16, 14, 9]
arr2 = arr[:]


for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 1
bump_all(arr, 4)
bump_if(arr, 2, 19, 2)
bump_all(arr, 2)
bump_if(arr, 1, 20, 3)
arr.reverse()
arr[4] -= 2
arr[4], arr[1] = arr[1], arr[4]
bump_all(arr, 5)
arr[9], arr[0] = arr[0], arr[9]
arr[3] -= 5
arr[5], arr[1] = arr[1], arr[5]
arr[4], arr[2] = arr[2], arr[4]
arr[1] -= 7
bump_all(arr, 1)
arr[9:10] = sorted(arr[9:10])
bump_if(arr, 4, 16, 4)
arr[6] += 4
arr[6] += 5
arr[5] += 7

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
