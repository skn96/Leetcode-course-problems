# Given two sorted integer arrays arr1 and arr2,
# return a new array that combines both of them and is also sorted.

arr1 = [1, 3, 7, 11]
arr2 = [-2, 4, 7, 13, 15]
arr_combined = []

n1 = len(arr1)
n2 = len(arr2)
n = n1 + n2

i = 0
j = 0

while i < n1 and j < n2:
    if arr1[i] <= arr2[j]:
        arr_combined.append(arr1[i])
        i += 1

    else:
        arr_combined.append(arr2[j])
        j += 1

while i < n1:
    arr_combined.append(arr1[i])
    i += 1

while j < n2:
    arr_combined.append(arr2[j])
    j += 1

for k in range(n):
    print(f"arr[{k}]: {arr_combined[k]}")
