def longest_mountain_sequence(arr):
    n = len(arr)
    inc, dec = [0] * n, [0] * n
    inc[0] = 1

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc[i] = inc[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            dec[i] = dec[i + 1] + 1
    
    max_length = 0
    for i in range(1, n - 1):
        if inc[i] > 1 and dec[i] > 0:
            max_length = max(max_length, inc[i] + dec[i] - 1)

    return max_length
