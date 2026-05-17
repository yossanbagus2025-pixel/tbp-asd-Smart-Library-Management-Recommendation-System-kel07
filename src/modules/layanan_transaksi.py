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
