counta = 0
countb = 0
countc = 0
for i in range(8):
    a = int(input())
    if a == 0:
        counta += 1
    elif 0 < a <= 50:
        countb += 1
    else:
        countc += 1
    
print("Zerados %d, até 50 unidades %d, acima de 50 unidades %d"%(counta,countb,countc))
