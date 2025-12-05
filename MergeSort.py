def merge(left, right):
    result = []
    i = j = 0

    # Merge while both halves have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any leftovers
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left, right)

arr = ([312, 1, 32, 4, 53, 412, 4,1 , 13, 31, 4, 41,3])
print(mergesort(arr))