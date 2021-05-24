def main():
    a = list(range(0,100))
    for i in range(len(a)):
        a = float(input())
        if (a <= 10):
            print("A[%d] ="%i,"%.1f"%a)
main()
