T  = int(input()) 
def fun_1():
    k = int(input())
    n = int(input())
   
    l = [[] for _ in range(k + 1)]
    
    for i in range(k + 1):
        for j in range(1, n + 1):
            if i == 0:
                l[i].append(j)
            else:
                l[i].append(sum(l[i - 1][:j]))
    
    print(l[k][-1])
    for i in range(k + 1):
        for j in range(1, n + 1):
            print(l[i][j - 1], end=" ")
        print()


for i in range(T):
    fun_1()