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
