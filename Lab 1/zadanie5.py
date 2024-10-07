# Zadanie 6
# Napisz skrypt sortujący liczby (dwoma wybranymi metodami). 
# Wygeneruj losowo N liczb - wykorzystaj standardową funkcję do losowania. 
# Z wbudowanej funkcji sortującej korzystaj tylko w celu weryfikacji wyników. 

import random

# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

N = 20
random_numbers = random.sample(range(1, 100), N)

sorted_quick = quicksort(random_numbers.copy())
sorted_merge = merge_sort(random_numbers.copy())
sorted_builtin = sorted(random_numbers)

print("Generated random numbers:")
print(random_numbers)
print("\nSorted using Quicksort:")
print(sorted_quick)
print("\nSorted using Merge Sort:")
print(sorted_merge)
print("\nSorted using built-in sorted function:")
print(sorted_builtin)