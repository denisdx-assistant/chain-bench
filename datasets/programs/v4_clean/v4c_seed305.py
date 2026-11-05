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
arr[2], arr[2] = arr[2], arr[2]
arr[4], arr[3] = arr[3], arr[4]
arr[0] += 40
arr2[3] = 47
arr[4] += 10
arr[9] += 56
"""


arr = [6, 19, 19, 13, 21, 22, 10, 17, 6, 23]
arr2 = arr[:]


for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 2
    else:
        arr[i] -= 4
arr[9] *= 2
bump_all(arr, 2)
arr[8] -= 2
arr[8] += 2
arr[2] += 2
bump_all(arr, 2)
arr[4], arr[2] = arr[2], arr[4]
arr.reverse()
bump_all(arr, 3)
arr[7] += 5
arr[5] -= 1
arr[9:10] = sorted(arr[9:10])
arr[4] += 3
arr.reverse()
for i in range(0, 10, 3):
    if arr[i] % 2 == 0:
        arr[i] += 5
    else:
        arr[i] -= 1
arr[0] += 9
arr[3], arr[0] = arr[0], arr[3]
bump_if(arr, 7, 15, 2)
arr[8] *= 2

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
