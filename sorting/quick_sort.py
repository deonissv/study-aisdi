def quick_sort(arr):
    less = []
    equal = []
    more = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                more.append(x)
        return quick_sort(less)+equal+quick_sort(more)
    return arr


def quick_sort_mem_save(arr):
    left = 0
    right = len(arr) - 1

    def recursion_base(arr, left, right):
        if left >= right:
            return

        q = partition(arr, left, right)
        recursion_base(arr, left, q-1)
        recursion_base(arr, q+1, right)

    def partition(arr, left, right):
        pivot_index = left
        pivot = arr[left]
        left += 1
        while left <= right:
            while left <= right and arr[left] <= pivot:
                left += 1
            while left <= right and arr[right] >= pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
        arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
        return right

    recursion_base(arr, left, right)
    return arr
