def main():
    a = float(input("Insira seu salario aqui: "))
    b = int(input("insira seu tempo de empresa(em anos): "))
    if(b >= 5):
        print("Seu novo salario e: ", a + a * 0.2)
    else:
        print("Voce nao precisa de bonus")

main()
