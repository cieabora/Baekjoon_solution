n = int(input())
if n % 2 == 1:
    result = 1
    for i in range(3, n + 1, 2):
        if i == 3:
            result = 4
        else:
            result *= 5
    print(result)
