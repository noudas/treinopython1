def sliptx(b,x):
    b = b.split()
    b1 = b[0]
    b2 = b[1]
    b1 = int(b1)
    b2 = int(b2)
    x.append(b1*b2)

a = int(input())
x = []
y = []
pum = []
for i in range(a):
    b = input()
    sliptx(b,x)
    b = input()
    sliptx(b,x)
    b = input()
    sliptx(b,x)
    b = input()
    sliptx(b,y)
    b = input()
    sliptx(b,y)
    b = input()
    sliptx(b,y)
    somax = sum(x)
    somay = sum(y)
    if somax > somay:
        pum.append("JOAO")
    elif somay > somax:
        pum.append("MARIA")
    else:
        pum.append("EMPATE")
    x = []
    y = []
    
for i in range(a):
    print(pum[i])
