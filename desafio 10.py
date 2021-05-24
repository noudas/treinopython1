def main():
    a = int(input("Insira um valor: "))
    b = int(input("Insira um valor: "))
    c = int(input("Insira um valor: "))
    if(a == b and b == c):
        print("Todos os numeros sao iguais")
    elif(a > b and a > c):
        if(c > b):
            print(a, " ", c, " ", b)
        elif(c > b):
            print(a, " ", b, " ", c)
    elif(b > a and b > c):
        if(c > a):
            print(b, " ", c, " ", a)
        elif(a > c):
            print(b, " ", a, " ", c)
    elif(c > a and c > b):
        if(b > a):
            print(c, " ", b, " ", a)
        elif(a > b):
            print(c, " ", a, " ", b)
    else:
        return False

main()
