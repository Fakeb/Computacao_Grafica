#1. Desenvolva uma aplicação em que o usuário insere os pontos referentes aos vértices de um triângulo (P0, P1 e P2),
# e então calcule, de acordo com um dos algoritmos de rasterização de linhas,
# os pontos que fazem parte das arestas do triângulo especificado.

#2. Escolha um dos algoritmos de rasterização de círculos. Está aplicação deverá:
# Pedir para o usuário informar o valor do raio do círculo (r);
# Pedir para o usuário informar o ponto central do círculo;
# A partir do raio e do ponto central, gerar os pontos (x,y) que formam o círculo e apresentar os mesmos na tela.

#3. Implemente uma aplicação que leia pelo teclado o raio de um círculo (r) e um ponto (x,y),
# e apresente na tela se o ponto está dentro ou fora do círculo. Considere que o ponto central do círculo está na origem.

#4. Desenvolva uma aplicação para geração de um circuíto automotivo a partir de 4 curvas de Bézier.
# Para isso, inicialmente gere aleatoriamente os 13 pontos que fazem parte da curva (P0, P1, P2... P12),
# sendo que P0, P3, P6, P9 e P12 são os pontos de ligação entre as curvas (e que P0 = P12, de modo a ser um circuíto fechado),
# e os demais são pontos de controle. 
# Após, defina a quantidade de segmentos a curva terá e então calcule os pontos que farão parte da mesma,
# apresentando o resultado na tela.

import random
import math
import os
clear = lambda: os.system('cls')

#Exercicio01
def exercicio01():
  print("Exercicio 01:\n")        
    
  Ponto0x = int(input('Digite o x do vértice P0 do triângulo: '))
  Ponto0y = int(input('Digite o y do vértice P0 do triângulo: '))
  Ponto1x = int(input('Digite o x do vértice P1 do triângulo: '))
  Ponto1y = int(input('Digite o y do vértice P1 do triângulo: '))
  Ponto2x = int(input('Digite o x do vértice P2 do triângulo: '))
  Ponto2y = int(input('Digite o y do vértice P1 do triângulo: '))

  for i in range(0,3):
    if i == 0:
      P0x = Ponto0x
      P0y = Ponto0y
      P1x = Ponto1x
      P1y = Ponto1y
      print('----- Ponto 0 até Ponto 1 -----')
    elif i == 1:
      P0x = Ponto0x
      P0y = Ponto0y
      P1x = Ponto2x
      P1y = Ponto2y
      print('\n----- Ponto 0 até Ponto 2 -----')
    else:
      P0x = Ponto1x
      P0y = Ponto1y
      P1x = Ponto2x
      P1y = Ponto2y
      print('\n----- Ponto 1 até Ponto 2 -----')

    deltaX = P1x - P0x
    deltaY = P1y - P0y

    if deltaX == 0: 
        print("A reta é vertical")
        y = P0y
        print("Pontos da reta:")
        while y <= P1y:
            print(P0x," , ",y)
            y = y+1

    else: 
        m = deltaY/deltaX
        b = P0y - m*P0x
        print("m = ",m)
        print("b = ",b)
        if m <= 1: 
            print("A reta está mais deitada")
            x = P0x
            print("Pontos da reta:")
            while(x <= P1x):
                y = m*x + b 
                print(x," , ",round(y))
                x = x+1
        elif m > 1: 
            print("A reta está mais de pé")
            y = P0y
            print("Pontos da reta: ")

            while(y <= P1y):
                x = (y-b)/m 
                print(round(x)," , ",y)
                y = y+1
  print("\n\n")

#Exercicio 02
def exercicio02():
  print("Exercicio 02:\n")        

  raioCirculo = int(input('Raio do Circulo: '))
  pontoCentralCirculo = int(input('Ponto central do circulo: '))

  raio = raioCirculo

  x = pontoCentralCirculo
  limite = raio * math.cos(math.radians(45))

  while x<=limite:
      y = math.sqrt(raio*raio - x*x) 
      print("(",x,",",round(y),")") 
      print("(",round(y),",",x,")") 
      print("(",round(y),",",-x,")") 
      print("(",x,",",-round(y),")") 
      print("(",-x,",",-round(y),")") 
      print("(",-round(y),",",-x,")") 
      print("(",-round(y),",",x,")") 
      print("(",-x,",",round(y),")") 
      x+=1

#Exercicio 03
def exercicio03():
  print("Exercicio 03:\n")        

  raioCirculo = int(input('Digite o raio do circulo:'))
  x = int(input('Digite o ponto x:'))
  y = int(input('Digite o ponto y:'))

  raio = raioCirculo

  pontoCentral = 0

  if (math.sqrt(x) + math.sqrt(y)) > math.sqrt(raio):
    print("O ponto está fora do círculo")
  else:
    print("O ponto está dentro do círculo")


def exercicio04():
    pontox = []
    pontoy = []

    i = 0
    j = 0

    pontox.append(random.randint(-5, 5))
    pontoy.append(random.randint(-5, 5))

    if pontox[0] >= 0 and pontoy[0] >= 0:
        for i in range(1,12):
            if i >= 4 and i <= 6:
                pontox.append(pontox[i-1]+random.randint(1,5))
            elif i > 8:
                pontox.append(pontox[i-1]-random.randint(30,40))
            else:
                pontox.append(pontox[i-1]+random.randint(1,5))
        
        for j in range(1,12):
            if j >= 4 and j <= 6:
                pontoy.append(pontoy[j-1]+random.randint(10,30))
            elif j > 8:
                pontoy.append(pontoy[j-1]-random.randint(10,30))
            else:
                pontoy.append(pontoy[j-1]+random.randint(1,5))

    elif pontox[0] < 0 and pontoy[0] < 0:
        for i in range(1,12):
            if i >= 4 and i <= 6:
                pontox.append(pontox[i-1]-random.randint(1,5))
            elif i > 8:
                pontox.append(pontox[i-1]+random.randint(30,40))
            else:
                pontox.append(pontox[i-1]-random.randint(1,5))
        
        for j in range(1,12):
            if j >= 4 and j <= 6:
                pontoy.append(pontoy[j-1]-random.randint(10,30))
            elif j > 8:
                pontoy.append(pontoy[j-1]+random.randint(10,30))
            else:
                pontoy.append(pontoy[j-1]-random.randint(1,5))

    else:
        for i in range(1,12):
            if i >= 4 and i <= 6:
                pontox.append(pontox[i-1]+random.randint(10,30))
            elif i > 8:
                pontox.append(pontox[i-1]-random.randint(10,30))
            else:
                pontox.append(pontox[i-1]+random.randint(1,5))
        
        for j in range(1,12):
            if j >= 4 and j <= 6:
                pontoy.append(pontoy[j-1]+random.randint(1,5))
            elif j > 8:
                pontoy.append(pontoy[j-1]-random.randint(30,40))
            else:
                pontoy.append(pontoy[j-1]+random.randint(1,5))

    pontox.append(pontox[0])
    pontoy.append(pontoy[0])

    i = 0

    for i in range(4):
        if i == 0:          
            P0x = pontox[0]
            P0y = pontoy[0]
            P1x = pontox[1]
            P1y = pontoy[1]
            P2x = pontox[2]
            P2y = pontoy[2]
            P3x = pontox[3]
            P3y = pontoy[3]
        elif i == 1:
            P0x = pontox[3]
            P0y = pontoy[3]
            P1x = pontox[4]
            P1y = pontoy[4]
            P2x = pontox[5]
            P2y = pontoy[5]
            P3x = pontox[6]
            P3y = pontoy[6]
        elif i == 2:      
            P0x = pontox[6]
            P0y = pontoy[6]
            P1x = pontox[7]
            P1y = pontoy[7]
            P2x = pontox[8]
            P2y = pontoy[8]
            P3x = pontox[9]
            P3y = pontoy[9]
        else:
            P0x = pontox[9]
            P0y = pontoy[9]
            P1x = pontox[10]
            P1y = pontoy[10]
            P2x = pontox[11]
            P2y = pontoy[11]
            P3x = pontox[12]
            P3y = pontoy[12]

        t = 0    
        while t<=1:         
            x = (1-t)*(1-t)*(1-t)*P0x + 3*(1-t)*(1-t)*t*P1x + 3*(1-t)*t*t*P2x + t*t*t*P3x
            y = (1-t)*(1-t)*(1-t)*P0y + 3*(1-t)*(1-t)*t*P1y + 3*(1-t)*t*t*P2y + t*t*t*P3y
            print("(",(x),",",(y),")")
            t +=0.01

#Menu
def menu():
  aux = False
  clear()
  while aux != True:
    
    op = input(
      "1 = Exercício 01,\n2 = Exercício 02,\n3 = Exercício 03,\n4 = Exercício 04,\n5 = Sair.\nInput: " 
    )

    if op == "1":
        clear()    
        exercicio01()
    elif op == "2":
        clear()
        exercicio02()
    elif op == "3":
        clear()
        exercicio03()
    elif op == "4":
        clear()
        exercicio04()
    elif op == "5":      
        print("\nSaiu!")
        aux = True
    else:        
        print("Nenhuma das opções selecionadas")

menu()