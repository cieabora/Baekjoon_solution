n = int(input())
m = int(input())
if m != 0:
    fixed = list(map(int, input().split()))
if m == 10:
    print(abs(n - 100))
elif n == 100:
    print(0)
elif m == 0:
    print(min(abs(n - 100), len(str(n))))
else:
    fixed.sort()
    fix = []
    for i in range(10):
        if i not in fixed:
            fix.append(i)
    num = str(n)
    done = True
    for i in range(len(num)):
        if int(num[i]) not in fix:
            done = False
            break
    if done:
        print(min(abs(n - 100), len(num)))
    else:
        tmp = 0
        next = 0
        result = abs(fix[0] - n) + len(str(fix[0]))
        done = True
        for a in [0] + fix:
            fix_1 = fix[:]
            if a == 0 and fix_1[0] != 0:
                fix_1 = [0] + fix_1
            for b in fix_1:
                fix_2 = fix[:]
                if b == 0 and fix_2[0] != 0:
                    fix_2 = [0] + fix
                for c in fix_2:
                    fix_3 = fix[:]
                    if c == 0 and fix_3[0] != 0:
                        fix_3 = [0] + fix
                    for d in fix_3:
                        fix_4 = fix[:]
                        if d == 0 and fix_4[0] != 0:
                            fix_4 = [0] + fix
                        for e in fix_4:
                            for f in fix:
                                if done:
                                    t_num = f + e * 10 + d * 10 ** 2 + c * 10 ** 3 + b * 10 ** 4 + a * 10 ** 5
                                    tmp = len(str(t_num)) + abs(t_num - n)
                                    if result > tmp:
                                        result = tmp
                                        
        print(min(abs(n - 100), result))