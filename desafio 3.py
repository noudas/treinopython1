def main():
    a = int(input("Insira um valor: "))
    b = int(input("Insira um valor: "))
    if(a > b):
        print(a - b)
    elif(b > a):
        print(b - a)
    else:
        print("numeros iguais")

main()
