def countMerge(arr, l, m, r):

    left = arr[l:m+1]
    right = arr[m+1:r+1]
    res, i,j, k = 0,0,0, l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            res += len(left) - i
            arr[k] = right[j]
            j += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return res


def countInv(arr, left, right):
    res = 0
    if left < right:
        m = (left+right) // 2
        res += countInv(arr, left, m)
        res += countInv(arr, m+1, right)
        res += countMerge(arr, left, m, right)


def intersection(a, b):
    n = len(a)
    m = len(b)
    i, j = 0, 0
    # print(n)

    while i < n and j < m:
        if a[i] == b[j]:
            print(a[i])
            i += 1
            j += 1
            while a[i] == a[i-1]:
                i += 1
                # print(f"i= {i}")
                if i == n-1:
                    break
            while b[j] == b[j-1]:
                j += 1
                # print(f"j = {j}")
                if j == m-1:
                    break
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
        # print(f"i = {i}, j = {j}")


if __name__ == '__main__':

    c = [3, 5, 10, 10, 10, 15, 15, 20]
    d = [5, 10, 10, 15, 30]

    e = [1, 1, 3, 3, 3]
    f = [1, 1, 1, 1, 3, 5, 7]

    g = [2, 20, 20, 40, 60]
    h = [10, 20, 20, 20]

    k = [40, 30, 20, 10]

    # intersection(g, h)
    print(countInv(k, 0, 3))
