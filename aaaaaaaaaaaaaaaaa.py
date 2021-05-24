a = float(input())
b = float(input())
c = float(input())
d = float(input())

a = a*2
b = b*3
c = c*4

e = (a+b+c+d)/10
print("Media: %.1f"%e)

if (e >= 7):
    print("Aluno aprovado.")
elif(e < 5):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    f = float(input())
    print("Nota do exame: %.1f"%f)
    f = (e+f)/2
    if (f >= 5):
        print("Aluno aprovado.")
        print("Media final: %.1f"%f)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f"%f)



