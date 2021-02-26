import math
#Algoritmo de Bézier de renderização de uma curva de grau 3

#pontos de controle:
P0x = 0
P0y = 0

P1x = -20
P1y = 20

P2x = 16
P2y = 0

P3x = 10
P3y = 10

t = 0

#calcula o ponto da curva para o valor de t correspondente
while t<=1:
    #para calcular o x, utitliza-se o x dos pontos de controle
    x = (1-t)*(1-t)*(1-t)*P0x + 3*(1-t)*(1-t)*t*P1x + 3*(1-t)*t*t*P2x + t*t*t*P3x

    #para calcular o y, utitliza-se o y dos pontos de controle
    y = (1-t)*(1-t)*(1-t)*P0y + 3*(1-t)*(1-t)*t*P1y + 3*(1-t)*t*t*P2y + t*t*t*P3y

    #mostra o ponto na tela
    print("(",(x),",",(y),")")
    #incrementa o t em uma certa quantia que, quanto menor, mais pontos serão gerados.
    t +=0.01