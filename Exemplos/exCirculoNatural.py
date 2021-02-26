import math
#Algoritmo de renderização de um círculo cujo ponto central é a origem

raio = 4

x = 0
limite = raio * math.cos(math.radians(45))

while x<=limite:
    y = math.sqrt(raio*raio - x*x) #y de "cima"
    yArred = round(y) #y arredondado para não precisar usar o round toda vez que dermos um print
    print("(",x,",",yArred,")") #x,y
    print("(",yArred,",",x,")") #y,x
    print("(",yArred,",",-x,")") #y,-x
    print("(",x,",",-yArred,")") #x,-y
    print("(",-x,",",-yArred,")") #-x,-y
    print("(",-yArred,",",-x,")") #-y,-x
    print("(",-yArred,",",x,")") #-y,x
    print("(",-x,",",yArred,")") #-x,y
    x+=1