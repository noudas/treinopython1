n = [1,2,3,4,5,6,7,8,9,10]
a = int(input())
for i in range(len(n)):
    n[i] = a
    print("X[%d] ="%i,a)
    a = a*2
    
