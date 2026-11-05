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
arr[6] *= 28
arr[2] *= 36
arr[1] = 4
arr2[3] = 1
arr[6], arr[6] = arr[6], arr[6]
arr[7] *= 3
"""


arr = [6, 5, 13, 12, 12, 26, 17, 9, 6, 14]
arr2 = arr[:]


arr[6] += 7
arr[4] *= 2
arr.reverse()
arr[8] += 3
bump_all(arr, 3)
arr.reverse()
arr[6], arr[9] = arr[9], arr[6]
arr[2] += 4
arr[4] *= 2
arr[5] -= 2
bump_all(arr, 3)
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 3
    else:
        arr[i] -= 5
arr[1:7] = sorted(arr[1:7])
bump_if(arr, 6, 17, 2)
bump_all(arr, 3)
arr[3] += 8
bump_if(arr, 8, 19, 2)
arr[0] += 5
arr[6] -= 6
arr[8:9] = sorted(arr[8:9])

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
