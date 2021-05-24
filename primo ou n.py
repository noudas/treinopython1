
a = []

def divisor(a):
    count = 2
    maximo = a // 2
    while count <= maximo:
        if (a % count == 0):
            return True
        count += 1
    return False


for i in range(int(input())):
    a.append(int(input()))

for j in range(len(a)):
    if divisor(a[j]) == True:
        print(a[j], "nao eh primo")
    else:
        print(a[j], "eh primo")
