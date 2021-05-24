a = int(input())
b = int(input())
c = 0

if (a - b >= 0):
    for i in range(a-1, b, -1):
        if(i % 2 != 0):
            c += i
    print(c)
            
elif(b - a >= 0):
    for i in range(b-1, a, -1):
        if(i % 2 != 0):
            c += i
    print(c)
            
else:
    print(c)

