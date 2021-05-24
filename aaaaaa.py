count = 0
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lista = [a,b,c,d,e]  

for i in range(len(lista)):
    if (lista[i] % 2 == 0):
        count += 1
    
print(count, "valores pares")
