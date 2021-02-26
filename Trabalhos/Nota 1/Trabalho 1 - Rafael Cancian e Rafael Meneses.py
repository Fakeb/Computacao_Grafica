import math
import os
clear = lambda: os.system('cls')

def calcularTriangulo(P0, P1, P2, P3, P4):
  t = 0
  while t<=1:
    x = (1-t)*P0[0] + t * P1[0]
    y = (1-t)*P0[1] + t * P1[1]
    z = (1-t)*P0[2] + t * P1[2] 
    print("(", x , "," , y , "," , z , ")")

    x = (1-t)*P0[0] + t * P2[0]
    y = (1-t)*P0[1] + t * P2[1]
    z = (1-t)*P0[2] + t * P2[2]
    print("(", x , "," , y , "," , z , ")")

    x = (1-t)*P0[0] + t * P4[0]
    y = (1-t)*P0[1] + t * P4[1]
    z = (1-t)*P0[2] + t * P4[2]
    print("(", x , "," , y , "," , z , ")")

    x = (1-t)*P1[0] + t * P3[0]
    y = (1-t)*P1[1] + t * P3[1]
    z = (1-t)*P1[2] + t * P3[2]
    print("(", x , "," , y , "," , z , ")")

    x = (1-t)*P1[0] + t * P4[0]
    y = (1-t)*P1[1] + t * P4[1]
    z = (1-t)*P1[2] + t * P4[2]
    print("(", x , "," , y , "," , z , ")")

    x = (1-t)*P2[0] + t * P3[0]
    y = (1-t)*P2[1] + t * P3[1]
    z = (1-t)*P2[2] + t * P3[2]
    print("(", x , "," , y , "," , z , ")")

    x = (1-t)*P2[0] + t * P4[0]
    y = (1-t)*P2[1] + t * P4[1]
    z = (1-t)*P2[2] + t * P4[2]
    print("(", x , "," , y , "," , z , ")")

    x = (1-t)*P3[0] + t * P4[0]
    y = (1-t)*P3[1] + t * P4[1]
    z = (1-t)*P3[2] + t * P4[2]
    print("(", x , "," , y , "," , z , ")")

    t +=0.01
   
def multiplicarMatrizar(matrizA, matrizB):
  matrizC = [0,0,0,0]
  i = 0
  j = 0
  while i < 4:
    j = 0
    while j < 4:
      matrizC[i] += matrizA[i][j] * matrizB[j] 
      j = j +1
    i = i +1
  return matrizC

P0 = [2.0, 0.0, 0.0]
P1 = [0.0, 2.0, 0.0]
P2 = [0.0, -2.0, 0.0]
P3 = [-2.0, 0.0, 0.0]
P4 = [0.0, 0.0, 4.0]
camera = [-10.0, 0.0, 0.0]

Menu = 1
while Menu != 0:
  Menu = int(input("\nTrabalho 1 – Câmera Virtual - Pipeline de Visualização 3D\n\n1 - Manipular objeto\n2 - Manipular a câmera\n3 - Modificar projeção\n4 - Modificar mapeamento\n5 - Visualizar objeto\n0 - Sair\n\nResposta: "))

  if Menu == 1:
    clear()
    Resposta = int(input("Manipular objeto\n\n1 - Translação\n2 - Escala\n3 - Rotação em X\n4 - Rotação em Y\n5 - Rotação em Z\n\nResposta: "))

    if Resposta == 1:
      Translação = int(input("Digite a translação: "))
      i=0
      while i < 3:
        P0[i] += Translação
        P1[i] += Translação
        P2[i] += Translação
        P3[i] += Translação
        P4[i] += Translação
        i += 1

    elif Resposta == 2:
      i=0
      while i < 3:
        P0[i] *= 2
        P1[i] *= 2
        P2[i] *= 2
        P3[i] *= 2
        P4[i] *= 2
        i += 1

    elif Resposta == 3:
      teta = int(input("Digite o teta: "))
      Pitch = [[1.0, 0.0, 0.0, 0.0], [0.0, math.cos(teta), (-1)*math.sin(teta), 0.0 ], [0.0 , math.sin(teta), math.cos(teta), 0.0], [0.0 ,0.0 ,0.0 ,1.0] ]

      Rx0 = [P0[0], P0[1] ,P0[2], 1.0]
      Rx1 = [P1[0], P1[1] ,P1[2], 1.0]
      Rx2 = [P2[0], P2[1] ,P2[2], 1.0]
      Rx3 = [P3[0], P3[1] ,P3[2], 1.0]
      Rx4 = [P4[0], P4[1] ,P4[2], 1.0]

      Rx0 = multiplicarMatrizar(Pitch, Rx0)
      P0[0] = Rx0[0]
      P0[1] = Rx0[1] 
      P0[2] = Rx0[2]
      
      Rx1 = multiplicarMatrizar(Pitch, Rx1)
      P1[0] = Rx1[0]
      P1[1] = Rx1[1] 
      P1[2] = Rx1[2]

      Rx2 = multiplicarMatrizar(Pitch, Rx2)
      P2[0] = Rx2[0]
      P2[1] = Rx2[1] 
      P2[2] = Rx2[2]

      Rx3 = multiplicarMatrizar(Pitch, Rx3)
      P3[0] = Rx3[0]
      P3[1] = Rx3[1] 
      P3[2] = Rx3[2]

      Rx4 = multiplicarMatrizar(Pitch, Rx4)
      P4[0] = Rx4[0]
      P4[1] = Rx4[1] 
      P4[2] = Rx4[2]

    elif Resposta == 4:
      teta = int(input("Digite o teta: "))
      Yaw = [[math.cos(teta), 0.0, math.sin(teta), 0.0], [0.0, 1, 0, 0.0 ], [(-1) *  math.sin(teta) ,0, math.cos(teta), 0.0], [0.0 ,0.0 ,0.0 ,1.0] ]

      Rx0 = [P0[0], P0[1] ,P0[2], 1.0]
      Rx1 = [P1[0], P1[1] ,P1[2], 1.0]
      Rx2 = [P2[0], P2[1] ,P2[2], 1.0]
      Rx3 = [P3[0], P3[1] ,P3[2], 1.0]
      Rx4 = [P4[0], P4[1] ,P4[2], 1.0]

      Rx0 = multiplicarMatrizar(Yaw, Rx0)
      P0[0] = Rx0[0]
      P0[1] = Rx0[1] 
      P0[2] = Rx0[2]
      
      Rx1 = multiplicarMatrizar(Yaw, Rx1)
      P1[0] = Rx1[0]
      P1[1] = Rx1[1] 
      P1[2] = Rx1[2]

      Rx2 = multiplicarMatrizar(Yaw, Rx2)
      P2[0] = Rx2[0]
      P2[1] = Rx2[1] 
      P2[2] = Rx2[2]

      Rx3 = multiplicarMatrizar(Yaw, Rx3)
      P3[0] = Rx3[0]
      P3[1] = Rx3[1] 
      P3[2] = Rx3[2]

      Rx4 = multiplicarMatrizar(Yaw, Rx4)
      P4[0] = Rx4[0]
      P4[1] = Rx4[1] 
      P4[2] = Rx4[2]

    elif Resposta == 5:
      teta = int(input("Digite o teta: "))
      Roll = [[math.cos(teta), (-1) *  math.sin(teta), 0, 0.0], [math.sin(teta), math.cos(teta), 0, 0.0 ], [0 ,0, 1, 0.0], [0.0 ,0.0 ,0.0 ,1.0] ]

      Rx0 = [P0[0], P0[1] ,P0[2], 1.0]
      Rx1 = [P1[0], P1[1] ,P1[2], 1.0]
      Rx2 = [P2[0], P2[1] ,P2[2], 1.0]
      Rx3 = [P3[0], P3[1] ,P3[2], 1.0]
      Rx4 = [P4[0], P4[1] ,P4[2], 1.0]

      Rx0 = multiplicarMatrizar(Roll, Rx0)
      P0[0] = Rx0[0]
      P0[1] = Rx0[1] 
      P0[2] = Rx0[2]
      
      Rx1 = multiplicarMatrizar(Roll, Rx1)
      P1[0] = Rx1[0]
      P1[1] = Rx1[1] 
      P1[2] = Rx1[2]

      Rx2 = multiplicarMatrizar(Roll, Rx2)
      P2[0] = Rx2[0]
      P2[1] = Rx2[1] 
      P2[2] = Rx2[2]

      Rx3 = multiplicarMatrizar(Roll, Rx3)
      P3[0] = Rx3[0]
      P3[1] = Rx3[1] 
      P3[2] = Rx3[2]

      Rx4 = multiplicarMatrizar(Roll, Rx4)
      P4[0] = Rx4[0]
      P4[1] = Rx4[1] 
      P4[2] = Rx4[2]

  elif Menu == 2:
    clear()
    Resposta = int(input("Manipular a câmera\n\n1 - Translação\n2 - Rotação em X\n3 - Rotação em Y\n4 - Rotação em Z\n\nResposta: "))

    if Resposta == 1:
      Translação = int(input("Digite a translação: "))
      i=0
      while i < 3:
        camera[i] += Translação
        i += 1
      print(camera)

    elif Resposta == 2:
      teta = int(input("Digite o teta: ")) * -1
      Pitch = [[1.0, 0.0, 0.0, 0.0], [0.0, math.cos(teta), (-1)*math.sin(teta), 0.0 ], [0.0 , math.sin(teta), math.cos(teta), 0.0], [0.0 ,0.0 ,0.0 ,1.0] ]

      RxC = [camera[0], camera[1] , camera[2], 1.0]


      RxC = multiplicarMatrizar(Pitch, RxC)
      camera[0] = RxC[0]
      camera[1] = RxC[1] 
      camera[2] = RxC[2]
      
      print(camera)

    elif Resposta == 3:
      teta = int(input("Digite o teta: ")) * -1
      Yaw = [[math.cos(teta), 0.0, math.sin(teta), 0.0], [0.0, 1, 0, 0.0 ], [(-1) *  math.sin(teta) ,0, math.cos(teta), 0.0], [0.0 ,0.0 ,0.0 ,1.0] ]

      RxC = [camera[0], camera[1] , camera[2], 1.0]


      RxC = multiplicarMatrizar(Yaw, RxC)
      camera[0] = RxC[0]
      camera[1] = RxC[1] 
      camera[2] = RxC[2]
      
      print(camera)

    elif Resposta == 4:
      teta = int(input("Digite o teta: ")) * -1
      Roll = [[math.cos(teta), (-1) *  math.sin(teta), 0, 0.0], [math.sin(teta), math.cos(teta), 0, 0.0 ], [0 ,0, 1, 0.0], [0.0 ,0.0 ,0.0 ,1.0] ]

      RxC = [camera[0], camera[1] , camera[2], 1.0]


      RxC = multiplicarMatrizar(Roll, RxC)
      camera[0] = RxC[0]
      camera[1] = RxC[1] 
      camera[2] = RxC[2]
      
      print(camera)

  elif Menu == 3:
    clear()
    Resposta = int(input("Modificar projeção\n\n1 - Projeção perspectiva\n2 - Projeção paralela\n\nResposta: "))

    if Resposta == 1:
      fovy = int(input("Digite o FOVY: "))
      width = int(input("Digite a largura da área de visualização: "))
      height = int(input("Digite a altura da área de visualização: "))
      aspect = width/height
      zNear = -1
      while zNear < 0:
        zNear = int(input("Digite a distância do observador inicial (maior que 0): ")) 
      zFar = -1
      while zFar < 0:
        zFar = int(input("Digite a distância do observador final (maior que 0): ")) 

      MatrizPerspectiva = [[ 1/(math.tan((fovy/2))*aspect ) , 0.0, 0.0, 0.0], [0.0, 1/(math.tan((fovy/2)) ), 0, 0.0 ], [ 0.0 , 0.0 , (zFar+zNear)/(zNear-zFar), (2*zFar*zNear)/(zNear*zFar) ], [0.0 ,0.0 ,-1.0 ,0.0] ]
      print(MatrizPerspectiva)

    elif Resposta == 2:
      left = int(input("Digite o valor esquerdo do x: "))
      right = int(input("Digite o valor direito do x: "))

      top = int(input("Digite o valor de cima do y: "))
      bottom = int(input("Digite o valor de baixo do y: "))

      near = -1
      while near < 0:
        near = int(input("Digite a distância do observador inicial do z (maior que 0): ")) 
      far = -1
      while far < 0:
        far = int(input("Digite a distância do observador final do z (maior que 0): "))

      MatrizParalela = [[ 2/(right-left)  , 0.0, 0.0, (-1)* ((right+left)/(right-left) ) ], [0.0, 2/(top-bottom), 0, (-1)* ((top+bottom)/(top-bottom) ) ], [ 0.0 , 0.0 , (-1)* (2/ ( far-near )), (-1)* ((far+near)/(far-near) )], [0.0 ,0.0 ,0.0 ,1.0] ]
      print(MatrizParalela)

  elif Menu == 4:
    clear()
    Resposta = int(input("Modificar mapeamento\n\n1 - Windows\n2 - Viewport\n\nResposta: "))

    if Resposta == 1:
      xminw = -1
      xmaxw = 1 
      yminw = -1
      ymaxw = 1

      xminw = int(input("Digite o valor mínimo de x: "))
      xmaxw = int(input("Digite o valor máximo de x: "))
      yminw = int(input("Digite o valor mínimo de y: "))
      ymaxw = int(input("Digite o valor mínimo de y: "))

    elif Resposta == 2:
      xminv = 0
      xmaxv = 500 
      yminv = 0
      ymaxv = 500

      xminv = int(input("Digite o valor mínimo de x: "))
      xmaxv = int(input("Digite o valor máximo de x: "))
      yminv = int(input("Digite o valor mínimo de y: "))
      ymaxv = int(input("Digite o valor mínimo de y: "))

  elif Menu == 5:
    clear()
    calcularTriangulo(P0, P1, P2, P3, P4)
