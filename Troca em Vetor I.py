n = list(range(0,20))
x = []
for i in range(len(n)):
    a = int(input())
    x.append(a)
b = x[::-1]
for i in range(len(n)):
    print("N[%d] ="%i,b[i])
