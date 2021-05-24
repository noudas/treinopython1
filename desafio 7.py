def main():
    a = float(input("Insira sua altura em m: "))
    b = input("Voce e M ou F? ")
    if(b == "M" or b == "m"):
        print("Seu peso ideal e: ", ((72.7 * a)- 58))
    elif(b == "F" or b == "f"):
        print("Seu peso ideal e: ", ((62.1 * a)- 44.7))
    else:
        print("Oof")
        return False


main()
