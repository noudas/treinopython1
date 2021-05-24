import random

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0 
count10 = 0

x = []

for i in range(10000):
    a = random.randint(1,10)
    x.append(a)
    if x[i] == 1:
        count1 += 1
    elif x[i] == 2:
        count2 += 1
    elif x[i] == 3:
        count3 += 1
    elif x[i] == 4:
        count4 += 1
    elif x[i] == 5:
        count5 += 1
    elif x[i] == 6:
        count6 += 1
    elif x[i] == 7:
        count7 += 1
    elif x[i] == 8:
        count8 += 1
    elif x[i] == 9:
        count9 += 1
    else:
        count10 += 1

    
print("O numero 1 apareceu %d vezes" %count1)
print("O numero 1 apareceu %d vezes" %count2)
print("O numero 1 apareceu %d vezes" %count3)
print("O numero 1 apareceu %d vezes" %count4)
print("O numero 1 apareceu %d vezes" %count5)
print("O numero 1 apareceu %d vezes" %count6)
print("O numero 1 apareceu %d vezes" %count7)
print("O numero 1 apareceu %d vezes" %count8)
print("O numero 1 apareceu %d vezes" %count9)
print("O numero 1 apareceu %d vezes" %count10)
