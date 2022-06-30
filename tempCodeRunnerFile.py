n, k = map(int, input().split())

m = max(n, k)
arr = dict()
arr[n] = 1

while k not in arr:
    for key in arr:
        temp = arr[key]
        if key >= 1:
            arr[key - 1] = temp + 1
        if key < 100000 and key + 1 not in arr:
            arr[key + 1] = temp + 1
        if key * 2 < 100000 and key * 2 not in arr:
            arr[key * 2] = temp + 1
print(arr[k] - 1)