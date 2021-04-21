def main():
    valor1= input("Escreva sua nota 1: ")
    while validanota(valor1):
        valor1= input("Escreva sua nota direito... ")
    valor2= input("Escreva sua nota 2: ")
    while validanota(valor2):
        valor2= input("Escreva sua nota direito... ")
    valor3= input("Escreva sua nota 3: ")
    while validanota(valor3):
        valor3= input("Escreva sua nota direito... ")
    valor4= input("Escreva sua nota 4: ")
    while validanota(valor4):
        valor4= input("Escreva sua nota direito... ")

    valortot = (float(valor1) + float(valor2) + float(valor3) + float(valor4))/4

    print("Sua media é: %.2f" %valortot)

    if (valortot <= 6):
        print("AEEEEEEEE PEGOU DP DISGRAÇA")
    else:
        print("AEEEEEEEE DESGRAÇA VC PASSOU!")



def validanota(nota):
    if(nota.isalpha() or nota == '' or nota == "."):
        return True
    elif(nota[0] == " "):
        return True
    elif(verificarletra(nota) == True):
        return True
    elif(verificar(nota) == False):
        if (0 >= float(nota) <= 10):
            return False
    else:
        return True
    
def verificar(nota):
    count = 0
    for i in range(len(nota)-1):
        if(nota[i] == "."):
            count+= 1
    if(count <= 1): 
        return False
    elif(count > 1):
        return True
    else:
        return True
    
def verificarletra(nota):
    count = 0
    for i in range(len(nota)-1):
        if(nota[i] == nota.isalpha()):
            count+= 1
    if(count <= 1):
        return False
    else:
        return True

main()
