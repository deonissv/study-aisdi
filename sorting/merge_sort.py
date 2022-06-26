def merge(arr1, arr2):
    ptr1 = 0
    ptr2 = 0
    res = []
    length1 = len(arr1)
    length2 = len(arr2)
    while ptr1 < length1 and ptr2 < length2:
        if arr1[ptr1] > arr2[ptr2]:
            res.append(arr2[ptr2])
            ptr2 += 1
        else:
            res.append(arr1[ptr1])
            ptr1 += 1
    while ptr1 < length1:
        res.append(arr1[ptr1])
        ptr1 += 1
    while ptr2 < length2:
        res.append(arr2[ptr2])
        ptr2 += 1

    return res


def merge_sort_recursive(arr):
    length = len(arr)

    if length > 1:

        mid = length // 2
        left_arr = arr[:mid]
        left_arr = merge_sort_recursive(left_arr)

        rigth_arr = arr[mid:]
        rigth_arr = merge_sort_recursive(rigth_arr)

        arr = merge(left_arr, rigth_arr)
    return arr


def merge_mem_save(arr, left, mid, right):
    tmp = []
    ptr_left = left
    ptr_right = mid
    while ptr_left < mid or ptr_right < right:
        if ptr_left == mid:
            tmp = tmp + arr[ptr_right: right]
            break
        if ptr_right == right:
            tmp = tmp + arr[ptr_left: mid]
            break
        if arr[ptr_left] > arr[ptr_right]:
            tmp.append(arr[ptr_right])
            ptr_right += 1
        else:
            tmp.append(arr[ptr_left])
            ptr_left += 1
    arr[left:right] = tmp
    return arr


def merge_sort_iterative(arr):
    length = len(arr)
    current_size = 1
    while current_size < length:
        current_index = 0
        while current_index < length:
            mid = current_index + current_size
            if mid < length:
                right = min(length, current_index + 2 * current_size)
                left = current_index
                merge_mem_save(arr, left, mid, right)

            current_index += 2 * current_size

        current_size *= 2
    return arr
