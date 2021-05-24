def main():

    a = input("Seu animal e mamifero(digite m), ave(gitite a) ou reptil(r) ")
    if(a == "m"):
        a = input("Seu animal e quadrupide(digite q), bipede(gitite b), voador(v) ou aquatico(a) ")
        if(a == "q"):
            a = input("Seu animal e herbivoro(h) ou carnivoro(c) ")
            if(a == "h"):
                print("Seu animal e o Cavalo")
            elif(a == "c"):
                print("Seu animal e o Leao")
            else:
                return False
    elif(a == "a"):
        print("a")
    elif(a == "r"):
        print("r")
    else:
        return False

main()
