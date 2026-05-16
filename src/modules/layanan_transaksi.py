def shell_sort_durasi(arr):
    """
    Big-O Worst : O(n²)
    Big-O Average: ~O(n^1.5)
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap].durasi_hari < temp.durasi_hari:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def merge_sort_frekuensi(arr):
    """Big-O: O(n log n)"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_frekuensi(arr[:mid])
    right = merge_sort_frekuensi(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """Big-O: O(n)"""
    res = []
    while left and right:
        if left[0].pinjam_count >= right[0].pinjam_count:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res + left + right
