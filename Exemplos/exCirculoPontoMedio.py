import math
#Algoritmo do Ponto Médio de renderização de um círculo cujo ponto central é a origem

def mostraPontos(x,y):
    print("(",x,",",y,")") #x,y
    print("(",y,",",x,")") #y,x
    print("(",y,",",-x,")") #y,-x
    print("(",x,",",-y,")") #x,-y
    print("(",-x,",",-y,")") #-x,-y
    print("(",-y,",",-x,")") #-y,-x
    print("(",-y,",",x,")") #-y,x
    print("(",-x,",",y,")") #-x,y

raio = 40

p = 1-raio

x = 0
y = raio
mostraPontos(x,y)

while True:
    if(p < 0): #x incrementa, e o próximo y não decrementa
        x+=1
        p = p + 2*x + 1
    elif(p >=0): #x incrementa e o próximo y decrementa
        x+=1
        y-=1
        p = p + 2*x - 2*y +1
    if x>=y: break
    mostraPontos(x,y)