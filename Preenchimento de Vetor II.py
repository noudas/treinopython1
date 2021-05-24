t = int(input())
x = []
for i in range(1000):
    x.append(i % t)

 
for i in range(1000):
    print("N[%d] ="%i,x[i])
