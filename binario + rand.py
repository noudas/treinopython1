import random
chama = 0

def abertura():
    return (x := random.randint(0,2**20))

def busca(maior,menor,a):
    meio = (menor + maior) // 2
    global chama
    chama += 1
    if (meio == a):
        print("O valor e ",meio)
    elif(meio > a):
        print("Seu numero inserido e Maior")
        return busca(meio-1,menor,a)
    else:
        print("Seu numero inserido e Menor")
        return busca(maior,meio+1,a)

def main():
    maior = 2**20
    menor = 0
    count = 0
    global chama
    while count < 10:
        chama = 0
        a = abertura()
        busca(maior,menor,a)
        count += 1
        print(chama)



main()
