def main():
    a = float(input("Insira seu salario: "))
    b = float(input("Insira a prestacao: "))
    if(b >= (0.3 * a)):
        print("Emprestimo nao concedido!")
    else:
        print("Emprestimo concedido")

main()
