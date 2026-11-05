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
arr2[9] = 14
arr[1] *= 44
arr[9] += 23
arr[3] += 58
arr[9], arr[5] = arr[5], arr[9]
arr2[7] = 57
"""


arr = [6, 29, 30, 2, 26, 23, 18, 25, 20, 20]
arr2 = arr[:]


arr[5] *= 2
arr[0] -= 9
arr.reverse()
arr[6] += 4
arr[5] -= 8
arr[8] += 7
arr.reverse()
arr[2] -= 9
arr[7] -= 5
arr[5:6] = sorted(arr[5:6])
bump_all(arr, 5)
arr.reverse()
arr[1] -= 6
bump_all(arr, 4)
arr[6] -= 6
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 5
    else:
        arr[i] -= 2
arr[1], arr[0] = arr[0], arr[1]
arr[6], arr[6] = arr[6], arr[6]
arr.reverse()
arr[8:9] = sorted(arr[8:9])

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
