def jogo(c,a):
    if a == c[i]:
        return "GAME OVER"
    elif int(c[i]) - int(c[i]) > a:
        return "GAME OVER"
    else:
        return "YOU WIN"

a, b = input().split()
c = input().split()
a = int(a)
b = int(b)


for i in range(b):
    if jogo(c,a) == "GAME OVER":
        break

print(jogo(c,a))

