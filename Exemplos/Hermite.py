import math
#Algoritmo de Hermite de renderização de uma curva de grau 3

#pontos de controle (ponto inicial e ponto final da curva de hermite):
P1x = 0
P1y = 0

P2x = 3
P2y = 3

#vetores tangente
#vetor que indica a força e a direção que a curva sai do ponto P1
M1x = 6 #tamanho do  vetor em X
M1y = -6 #tamanho do vetor em Y

#vetor que indica a força e a direção que a curva chega do ponto P2
M2x = -6 #tamanho do  vetor em X
M2y = -4 #tamanho do vetor em Y

t = 0

#calcula o ponto da curva para o valor de t correspondente
while t<=1:
    tAoCubo = t*t*t
    tAoQuad = t*t

    #para calcular o x, utitliza-se o x dos pontos de controle e dos vetores tangente
    x = (2*tAoCubo-3*tAoQuad+1)*P1x + (tAoCubo-2*tAoQuad+t)*M1x + (-2*tAoCubo+3*tAoQuad)*P2x + (tAoCubo-tAoQuad)*M2x

    #para calcular o y, utitliza-se o y dos pontos de controle e dos vetores tangente
    y = (2*tAoCubo-3*tAoQuad+1)*P1y + (tAoCubo-2*tAoQuad+t)*M1y + (-2*tAoCubo+3*tAoQuad)*P2y + (tAoCubo-tAoQuad)*M2y

    #mostra o ponto na tela
    print("(",(x),",",(y),")")
    #incrementa o t em uma certa quantia que, quanto menor, mais pontos serão gerados.
    t +=0.01