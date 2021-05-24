def main():
    a = float(input())
    b = float(input())
    c = float(input())
    pi = 3.14159
    
    d = ((a*c)/2)
    e = (pi*c*c)
    f = (((a+b)*c)/2)
    g = (b*b)
    h = (a*b)
    
    print("TRIANGULO: %.3f" %d)
    print("CIRCULO: %.3f" %e)
    print("TRAPEZIO: %.3f" %f)
    print("QUADRADO: %.3f" %g)
    print("RETANGULO: %.3f" %h)
    
main()
