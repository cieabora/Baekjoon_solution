n = int(input())
grade = list(map(int, input().split()))
m = max(grade)
print(sum(map(lambda a: a / m * 100, grade)) / n)
