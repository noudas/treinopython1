m = 0
p = 0
for i in range(0, 10, 1):
    a = int(input())
    if(a > m):
        m = a
        p = i+1

print("%d\n%d"%(m,p))
