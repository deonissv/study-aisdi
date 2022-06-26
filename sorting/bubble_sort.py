def bubble_sort(arr):
    length = len(arr) - 2
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(length):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
    return arr
