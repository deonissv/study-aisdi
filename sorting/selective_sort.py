def selective_sort(arr):
    for i in range(len(arr)):
        j = min_index(arr[i:])
        arr[i], arr[j+i] = arr[j+i], arr[i]
        i += 1
    return arr


def min_index(arr):
    min_value = arr[0]
    min_index = 0
    for i in range(len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
    return min_index
