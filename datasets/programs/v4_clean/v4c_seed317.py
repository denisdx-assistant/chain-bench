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
arr2[7] = 59
arr[4] *= 27
arr2[5] = 5
arr[6], arr[5] = arr[5], arr[6]
arr[3] *= 54
arr[0] = 49
"""


arr = [15, 1, 23, 25, 13, 1, 7, 8, 18, 15]
arr2 = arr[:]


arr[7], arr[1] = arr[1], arr[7]
bump_all(arr, 5)
arr[7] *= 2
arr[5] += 2
arr[4] += 1
arr.reverse()
arr.reverse()
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 1
bump_all(arr, 3)
arr[2] *= 2
arr[6], arr[9] = arr[9], arr[6]
bump_if(arr, 9, 16, 5)
arr.reverse()
arr[5], arr[5] = arr[5], arr[5]
arr[6] += 2
bump_all(arr, 5)
arr[1] *= 2
arr[6], arr[5] = arr[5], arr[6]
arr[0] += 8
bump_if(arr, 4, 17, 2)

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
