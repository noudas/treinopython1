i = 0
val = []
while i >= 0:
    i = int(input())
    if(i < 0):
        break
    val.append(i)
    print(val)
    
media = sum(val) / len(val)
print("%.2f"%media)
