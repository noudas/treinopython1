a = int(input())
while a > 0:    
    b = int(input())
    c = float(input())
    if b == 1:
        d = c*0.015
        print("Valor investido R$ %.2f"%c, "e Juros: R$ %.2f"%d)
    elif b==2:
        d = c*0.02
        print("Valor investido R$ %.2f"%c, "e Juros: R$ %.2f"%d)
    else:
        d = c*0.04
        print("Valor investido R$ %.2f"%c, "e Juros: R$ %.2f"%d)
    a = int(input())
        
