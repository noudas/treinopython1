a = []

def divisor(a):
    g = 0
    count = 1
    maximo = a // 2
    while count <= maximo:
        if (a % count == 0):
            g = g + count
        count += 1
    if(g == a):
        return True
    else:
        return False


for i in range(int(input())):
    a.append(int(input()))

for j in range(len(a)):
    if divisor(a[j]) == True:
        print(a[j], "eh perfeito")
    else:
        print(a[j], "nao eh perfeito")
