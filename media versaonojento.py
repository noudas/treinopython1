def main():
    notas = []
    qtd = 0
    x = verNota(input("Insira a a nota: "))
    while x[0] == True:
        notas.append(x[1])
        qtd += 1
        x = verNota(input("Insira %da nota: " %(qtd+1)))
    print("Média: %.2f" %media(notas, qtd))


def verNota(nota):
    cnt_num = 0
    cnt_pto = 0

    for i in range(len(nota)):
        if nota[i] == ".":
            cnt_pto += 1
            if cnt_pto > 1:
                print("Saída por excesso de pontos")
                return (False,)
            
        elif nota[i].isnumeric() == False:
            print("Saída por caractére especial ou letra")
            return (False,)
        
        cnt_num += 1

    if cnt_num == 0:
        print("Saída por inexistência de número")
        return (False,)

    #Isso pode ser considerado um número positivo de ponto flutuante
    nota = float(nota)
    
    if nota > 10:
        print("Saída por nota maior do que 10\nO número %f foi desconsiderado" %nota)
        return (False,)
    
    #Esse número é uma nota válida
    return (True, float(nota))

def media(nota, qtd):
    if (qtd > 0):
        return sum(nota)/qtd
    else:
        return (False,)


main()
