p0x=1
p0y=1

p1x=8
p1y=8

#1. Calculamos a diferença entre x’s e y’s dos dois pontos:
deltaX = p1x - p0x
deltaY = p1y - p0y

if deltaX == 0: #se deltaX for 0, é uma reta vertical
    print("A reta é vertical")
    y = p0y
    while y <= p1y:
        print(p0x," , ",y)
        y = y+1

else: #não é uma reta vertical, logo, calculamos a equação da reta
    m = deltaY/deltaX
    b = p0y - m*p0x
    print("m = ",m)
    print("b = ",b)
    if m <= 1: #a reta está mais deitada, logo, o x cresce mais rápido do que o y
        print("A reta está mais deitada")
        x = p0x
        while(x <= p1x):
            y = m*x + b #equação da reta em termos de x
            print(x," , ",round(y))
            x = x+1
    elif m > 1: #a reta está mais de pé, logo, o y cresce mais rápido do que o x
        print("A reta está mais de pé")
        y = p0y
        while(y <= p1y):
            x = (y-b)/m #equação da reta em termos de y
            print(round(x)," , ",y)
            y = y+1
