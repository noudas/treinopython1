def main():
    a = int(input("Insira a idade do nadador: "))
    if(a <= 5):
        print("Categoria: Bebe")
    elif(a > 5 and a <= 7):
        print("Categoria: Infantil A")
    elif(a >= 8 and a <= 10):
        print("Categoria: Infantil B")
    elif(a >= 11 and a <= 13):
        print("Categoria: Juvenil A")
    elif(a >= 14 and a <= 17):
        print("Categoria: Juvenil B")
    else:
        print("Categoria: Senior")


main()
