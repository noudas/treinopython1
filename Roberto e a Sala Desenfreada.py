while True:
    try:
        EPR = 0
        EHD = 0
        INTRUSOS = 0

        for i in range(int(input())):
            a = input().split()
            c = a[1]
            if c == "EPR":
                EPR += 1
            elif c == "EHD":
                EHD += 1
            else:
                INTRUSOS += 1
        

        print("EPR:",EPR)
        print("EHD:",EHD)
        print("INTRUSOS:",INTRUSOS)
        
    except EOFError:
        break
    
