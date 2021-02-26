import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import time
import PIL
from PIL import Image

Window = None
Shader_programm = None
Vao = None
WIDTH = 1000
HEIGHT = 720
luzinha = [0.1,0.1,0.1] #variavel para manipular luz secundaria
points = [] #pontos das vertices
normais = [] #pontos das normais
indicesVertices = 0 # numero de vertices
luzOn = 0 #ligar desligar luz
rotY = 0 #usado para girar o cenario
portaOn = 0 #usado para "abrir" a porta

Tempo_entre_frames = 0 #variavel utilizada para movimentar a camera

#Variáveis referentes a câmera virtual e sua projeção
Cam_speed = 5.0 #velocidade da camera, 1 unidade por segundo
Cam_yaw_speed = 30.0 #velocidade de rotação da câmera em y, 10 graus por segundo
Cam_pitch_speed = 30.0 #velocidade de rotação da câmera em x, 10 graus por segundo
Cam_pos = np.array([0.0, 2.0, 5.0]) #posicao inicial da câmera
Cam_yaw = 0.0 #ângulo de rotação da câmera em y
Cam_pitch = 0.5 # #ângulo de rotação da câmera em x

def leituraObj(nomeObj):
    global points, normais, indicesVertices

    arquivo = open(nomeObj, "r") #abrir o .obj

    #criação das variaveis para manipular valores do .obj
    vertices = []
    nvertices = []
    faces = []
    facesVertices = []
    facesNormais = []
    
    i=0
    j=0

    for linha in arquivo:

        valores = linha.split()#valores recebe uma lista sem espaços de vetores

        if valores[0] == "v": #verificar linha que começa com v
            valores.remove("v") #remove o v para inserir as linhas em vertices
            vertices.append(valores) #insere os valores em vertices
        elif valores[0] == "vn": #verificar linha que começa com vn
            valores.remove("vn") # remove o vn para inserir as linhas em nvertices
            nvertices.append(valores) #insere os valores em nvertices
        elif valores[0] == "f": #verificar linha que começa com f
            valores.remove("f") #remove o f para inserir as linhas em faces
            faces.append(valores) #insere os valores em faces
            indicesVertices += 1 #conta a quantidade de faces para fazer o calculo de quantas vertices tem nos objetos

            for j in range(len(faces[i])): # loop em volta do j até o final de posições do vetor[i] que esta dentro da lista(faces)

                aux = str(faces[i][j]) #variavel auxiliar que recebe os numeros da faces 
                j += 1 # incrementa em j
                facesVertices.append(aux[0:aux.find("//")]) # facesVertices recebe os valores de faces para ordenar as vertices 
                facesNormais.append(aux[aux.find("//")+2: len(aux) ]) # facesNormais recebe os valores de faces para ordenar as normais
            
            i += 1 #incrementa i
            j = 0 #reseta o j

    indicesVertices *= 3 #calculo para saber a quantidade de vertices do objeto

    i = 0 #reseta i
    aux = "" #reseta aux
    num = 0 #cria variavel num
    #pointsLer = []

    while i < len(facesVertices): #loop enquanto existir facesVertices
        num = int(facesVertices[i]) #num recebe o primeiro numero de facesVertices
        aux = vertices[num-1] #variavel auxiliar recebe valor de vertices na posiçao da variavel num -1(pois começa em 0)
        points.append(aux[0]) #insere as vertices ordenadas em points
        points.append(aux[1]) #insere as vertices ordenadas em points
        points.append(aux[2]) #insere as vertices ordenadas em points
        i +=1 #incrementa i

    i = 0 #reseta i
    aux = "" #reseta aux
    num = 0 #cria variavel num
    #normaisLer = []

    while i < len(facesNormais): #loop enquanto existir facesVertices
        num = int(facesNormais[i]) #num recebe o primeiro numero de facesVertices
        aux = nvertices[num-1] #variavel auxiliar recebe valor de vertices na posiçao da variavel num -1(pois começa em 0)
        normais.append(aux[0]) #insere as vertices ordenadas em points
        normais.append(aux[1]) #insere as vertices ordenadas em points
        normais.append(aux[2]) #insere as vertices ordenadas em points
        i +=1 #incrementa i

    # points += pointsLer
    # normais += normaisLer
    arquivo.close() #fecha o arquivo

def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT

    #Inicializa GLFW
    glfw.init()

    #Criação de uma janela
    Window = glfw.create_window(WIDTH, HEIGHT, "Exemplo - renderização de um triângulo", None, None)
    if not Window:
        glfw.terminate()
        exit()

    glfw.set_window_size_callback(Window, redimensionaCallback)
    glfw.make_context_current(Window)

    #print("Placa de vídeo: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    #print("Versão do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))

def inicializaObjetos():

    global Vao, points, normais
    # Vao do cubo
    Vao = glGenVertexArrays(1)
    glBindVertexArray(Vao)

    # VBO dos vértices do quadrado
    #os points sao recebidos globalmente pelo ler leituraObj
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    # VBO das normais
    #os normais sao recebidos globalmente pelo ler leituraObj
    normais = np.array(normais, dtype=np.float32)
    nvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, nvbo)
    glBufferData(GL_ARRAY_BUFFER, normais, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

    # VBO das texturas
    texcoords = points
    texcoords = np.array(texcoords, dtype=np.float32)
    tvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, tvbo)
    glBufferData(GL_ARRAY_BUFFER, texcoords, GL_STATIC_DRAW)
    glEnableVertexAttribArray(2)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, None)

def inicializaShaders():
    global Shader_programm
    # Especificação do Vertex Shader:
    #viewX criada para olhar para cima e para baixo
    vertex_shader = """
        #version 400
        layout(location = 0) in vec3 vertex_posicao;
        layout(location = 1) in vec3 vertex_normal;
        layout(location = 2) in vec2 vertex_textures;
        out vec3 vertex_posicao_cam, vertex_normal_cam;
        out vec2 textcoord;
        uniform mat4 matriz, viewy, viewx, proj;
        void main () {
            textcoord = vertex_textures;
            vertex_posicao_cam = vec3 (viewy * viewx * matriz * vec4 (vertex_posicao, 1.0)); //posição do objeto em relação a CÂMERA
            vertex_normal_cam = vec3 (viewy * viewx * matriz * vec4 (vertex_normal, 0.0)); //normais do objeto em relação a CÂMERA
            gl_Position = proj * viewy * viewx * matriz * vec4 (vertex_posicao, 1.0);
        }
    """
    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

    # Especificação do Fragment Shader:
    fragment_shader = """
        #version 400
		in vec3 vertex_posicao_cam, vertex_normal_cam;
        in vec2 textcoord;
        
        //propriedades de uma luz pontual
        uniform vec3 luz_posicao;
        uniform vec3 Ls;// luz especular
		uniform vec3 Ld;// luz difusa
		uniform vec3 La;// luz ambiente

        //propriedades de reflexão da superficie
		uniform vec3 Ks;//reflexão especular
		uniform vec3 Kd;//reflexão difusa
		uniform vec3 Ka;//reflexão ambiente
        uniform float especular_exp;//expoente especular
        
        uniform mat4 view;

        uniform sampler2D basic_texture;

		out vec4 frag_colour;
		void main () {
            /*
            Cálculo de Intensidade de Luz Ambiente (Ia)
            O cálculo da intensidade de luz ambiente é o mais simples:
            basta multiplicar a cor da luz ambiente pela refletância de luz ambiente da superfície
            */

            vec3 Ia = La * Ka;

            /*
            Cálculo de Intensidade de Luz Difusa (Id)
            Para calcularmos a intensidade de luz difusa, precisamos, primeiramente, 
            calcular a posição da luz em relação a câmera (luz_posicao_cam)
            */

            vec3 luz_posicao_cam = vec3 (view * vec4 (luz_posicao, 1.0));//posicao da luz em relação a câmera
            
            /*A posição da luz (luz_posicao_cam) calculada acima representa um vetor que sai da origem (0,0,0) e
		aponta para a luz. Para a luz difusa, precisamos calcular um vetor que saia de cada vértice do objeto
		(vertex_posicao_cam) e aponte para essa luz. Para isso, basta calcularmos a diferença entre luz_posicao_cam
		e vertex_posicao_cam.*/

            vec3 luz_vetor_cam = luz_posicao_cam - vertex_posicao_cam;//vetor apontando para a luz em relação a posicao do vértice 
            
            /*Por fim, normalizamos o vetor da luz em relação ao vértice do objeto e calculamos o cosseno do angulo
		entre o mesmo e a normal da superficie utilizando o produto escalar*/

            vec3 luz_vetor_cam_normalizada = normalize(luz_vetor_cam);//vetor da luz normalizada
            vec3 vertex_normal_cam_normalizada = normalize(vertex_normal_cam);
            float cosseno_difusa = dot(vertex_normal_cam_normalizada,luz_vetor_cam_normalizada);//cosseno do angulo entre o vetor da luz e a normal da superficie
            
            vec3 Id = Ld * Kd * cosseno_difusa;

            /*
            Cálculo de Intensidade de Luz Especular (Is)
            Para o cálculo da intensidade de luz especular, precisamos primeiramente calcular o vetor que representa 
            a luz refletida em relação a normal da superfície */

            vec3 luz_reflexao_vetor_cam = reflect(-luz_vetor_cam_normalizada, vertex_normal_cam_normalizada);
            
            /*Como a intensidade de luz especular depende da posição da câmera, definimos um vetor que sai da superficie
		    do objeto e aponta para a camera, e então normalizamos, pois utilizaremos ele no cálculo do produto escalar*/
            
            vec3 superficie_camera_vetor = normalize(-vertex_posicao_cam);

            /*E então calculamos o ângulo entre o vetor de reflexão da luz e o vetor em relação a posicao do observador*/
            
            float cosseno_especular = dot(luz_reflexao_vetor_cam, superficie_camera_vetor);
            cosseno_especular = max(cosseno_especular, 0.0);//se o cosseno der negativo, atribui 0 para ele
            
            /*Na intensidade especular, precisamos elevar o cosseno calculado acima ao expoente especular*/
            
            float fator_especular = pow (cosseno_especular, especular_exp);
            
            /*E, por fim, calculamos a intensidade de luz especular refletida (Is) */

            vec3 Is = Ls * Ks * fator_especular;

            /*A cor final do fragmento é a soma das 3 componentes de iluminação*/
		    
            vec4 texel = texture(basic_texture, textcoord);

            frag_colour = texel * vec4 (Ia+Id+Is,1.0);
		}
    """
    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
    Shader_programm = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def transformaCubo(tx, ty, tz, sx, sy, sz, rx, ry, rz):
    #matriz de translação
    translacao = np.array([
        [1.0, 0.0, 0.0, tx], 
        [0.0, 1.0, 0.0, ty], 
        [0.0, 0.0, 1.0, tz], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    #matriz de escala
    escala = np.array([
        [sx, 0.0, 0.0, 0.0], 
        [0.0, sy, 0.0, 0.0], 
        [0.0, 0.0, sz, 0.0], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    #matriz de rotação em torno do eixo X
    angulo = np.radians(rx)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoX= np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, cos, -sen, 0.0],
        [0.0, sen, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #matriz de rotação em torno do eixo Y
    angulo = np.radians(ry)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoY= np.array([
        [cos, 0.0,sen, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-sen, 0.0, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #matriz de rotação em torno do eixo Z
    angulo = np.radians(rz)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoZ= np.array([
        [cos, -sen, 0.0, 0.0],
        [sen, cos, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #combinacao das rotacoes
    rotacoes = rotacaoZ.dot(rotacaoY.dot(rotacaoX)) #rotação em X primeiro, seguido de Y, seguido de Z

    #matriz de transformação do cubo combinando translação, escala e as 3 rotações
    transformacao = translacao.dot(escala.dot(rotacoes)) #rotacao primeiro, escala em seguida, , translação depois

    #E passamos a matriz para o Vertex Shader.
    transformLoc = glGetUniformLocation(Shader_programm, "matriz")
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transformacao)

def especificaMatrizVisualizacao():

    # Especificação da matriz de visualização, que é definida com valores de translação e
	# rotação inversos da "posição" da câmera, pois é o mundo que se movimenta ao redor da
	# câmera, e não a câmera que se movimenta ao redor do mundo.
    #visualizacao = np.identity(4)

    #posicao da camera
    translacaoCamera = np.array([
    [1.0, 0.0, 0.0, -Cam_pos[0]], 
    [0.0, 1.0, 0.0, -Cam_pos[1]], 
    [0.0, 0.0, 1.0, -Cam_pos[2]], 
    [0.0, 0.0, 0.0, 1.0]], np.float32)
    
    #orientacao da camera (rotação em y)
    angulo = np.radians(-Cam_yaw)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoCameraY = np.array([
        [cos, 0.0, sen, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-sen, 0.0, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #orientacao da camera (rotação em x) para fazer a camera olhar para cima e para baixo
    angulo = np.radians(-Cam_pitch)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoCameraX = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, cos, -sen, 0.0],
        [0.0, sen, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #criaçao de variaveis para fazer o calculo no shader, tentei fazer reutilizando as variaveis, mas deu problema.
    visualizacaoY = rotacaoCameraY.dot(translacaoCamera)
    visualizacaoX = rotacaoCameraX.dot(translacaoCamera)
    transformLocY = glGetUniformLocation(Shader_programm, "viewy")
    transformLocX = glGetUniformLocation(Shader_programm, "viewx")
    glUniformMatrix4fv(transformLocY, 1, GL_TRUE, visualizacaoY)
    glUniformMatrix4fv(transformLocX, 1, GL_TRUE, visualizacaoX)
    
def especificaMatrizProjecao():
    #Especificação da matriz de projeção perspectiva.
    znear = 0.1 #recorte z-near
    zfar = 100.0 #recorte z-far
    fov = np.radians(67.0) #campo de visão
    aspecto = WIDTH/HEIGHT #aspecto

    a = 1/(np.tan(fov/2)*aspecto)
    b = 1/(np.tan(fov/2))
    c = (zfar + znear) / (znear - zfar)
    d = (2*znear*zfar) / (znear - zfar)
    projecao = np.array([
        [a,   0.0, 0.0,  0.0],
        [0.0, b,   0.0,  0.0],
        [0.0, 0.0, c,    d],
        [0.0, 0.0, -1.0, 1.0]
    ])

    transformLoc = glGetUniformLocation(Shader_programm, "proj")
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, projecao)

def inicializaCamera():
    especificaMatrizVisualizacao()
    especificaMatrizProjecao()

def trataTeclado():
    global Cam_pos, Cam_yaw, Cam_yaw_speed, Tempo_entre_frames, luzinha, Cam_pitch, Cam_pitch_speed, luzOn, points, normais, rotY, portaOn
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)):
            glfw.set_window_should_close(Window, True)

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_A)):
        Cam_pos[0] -= Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_D)):
        Cam_pos[0] += Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_PAGE_UP)):
        Cam_pos[1] += Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_PAGE_DOWN)):
        Cam_pos[1] -= Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_W)):
        Cam_pos[2] -= Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_S)):
        Cam_pos[2] += Cam_speed * Tempo_entre_frames

    if(glfw.get_cursor_pos(Window)[0] < int(glfw.get_window_size(Window)[0])/3): #pega a posição do mouse e compara para girar a camera
        Cam_yaw += Cam_yaw_speed * Tempo_entre_frames

    if(glfw.get_cursor_pos(Window)[0] > int(glfw.get_window_size(Window)[0])/1.7): #pega a posição do mouse e compara para girar a camera
        Cam_yaw -= Cam_yaw_speed * Tempo_entre_frames
    
    if(glfw.get_cursor_pos(Window)[1] < int(glfw.get_window_size(Window)[1])/3): #pega a posição do mouse e compara para girar a camera
        if(Cam_pitch <= 50): #para a camera nao "girar a cabeça para cima" alem do "maximo"
            Cam_pitch += Cam_pitch_speed * Tempo_entre_frames

    if(glfw.get_cursor_pos(Window)[1] > int(glfw.get_window_size(Window)[1])/1.3): #pega a posição do mouse e compara para girar a camera
        if(Cam_pitch >= -70): #para a camera nao "girar a cabeça para baixo" alem do "minimo"
            Cam_pitch -= Cam_pitch_speed * Tempo_entre_frames

    #usado para aumentar ou diminuir a luz do ambiente
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_L)):     
        if(luzOn == 0):
            luzinha = [1.0,1.0,1.0]
            time.sleep(0.5)
            luzOn = 1
        elif(luzOn == 1):
            luzinha = [0.1,0.1,0.1]
            luzOn = 0
            time.sleep(0.5)
    
    #a ideia inicial era girar a porta, mas como o objeto inteiro ta dentro do points, e por outros detalhes, nao consegui renderizar um objeto separadamente
    #entao a cena some e aparece com a porta fechada e aberta
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_P)):
        points = []
        normais = []
        if(portaOn == 0):
            portaOn = 1
            leituraObj("CasaPortaFechadaSemSofa.obj")
            inicializaObjetos()
            time.sleep(1)
        elif(portaOn == 1):
            portaOn = 1
            leituraObj("CasaPortaAbertaSemSofa.obj")
            inicializaObjetos()
            time.sleep(1)

    #usado para girar a cena, ja que a camera nao esta perfeita, se virada para tras, os comandos wasd sao invertidos
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_KP_ADD)):
        rotY += 1
           
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_KP_SUBTRACT)):
        rotY -= 1
        
def inicializaTexturas():
    global textura, Shader_programm
    
    #carrega a imagem
    img = Image.open("gradient.png").transpose(Image.FLIP_TOP_BOTTOM)
    img_data = np.frombuffer(img.tobytes(), np.uint8) #converte o arquivo em bytes
    width, height = img.size #pega a largura e altura da imagem

    #gera a textura para a imagem
    textura = glGenTextures(1) #gera um id para a textura
    glBindTexture(GL_TEXTURE_2D, textura) #ativa a textura criada a cima
    #como a textura "embrulha" o objeto
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    #com qual qualidade a textura "embrulha" o objeto
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) #qual a qualidade que uma textura grande diminui o seu tamanho
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) #qual a qualidade que uma textura pequena aumenta o seu tamanho
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data) #gera a textura OpenGL a partir da imagem
    #glGenerateMipmap(GL_TEXTURE_2D) #gera a textura OpenGL a partir da imagem

def ativaTextura():
    #glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textura)
    texture_loc = glGetUniformLocation(Shader_programm, "basic_texture")
    glUniform1i(texture_loc, 0)

def especificaMaterialCubo(KaR, KaG, KaB, KdR, KdG, KdB, KsR, KsG, KsB, n):
    global Shader_programm
    #Coeficiente de reflexão ambiente
    Ka = np.array([KaR, KaG, KaB])#reflete 100% da luz ambiente
    Ka_loc = glGetUniformLocation(Shader_programm, "Ka")
    glUniform3fv(Ka_loc, 1, Ka)

    #Coeficiente de reflexão difusa
    Kd = np.array([KdR, KdG, KdB])#reflete luz difusa 
    Kd_loc = glGetUniformLocation(Shader_programm, "Kd")
    glUniform3fv(Kd_loc, 1, Kd)

    #Coeficiente de reflexão especular
    Ks = np.array([KsR, KsG, KsB])#reflete 100% da luz especular
    Ks_loc = glGetUniformLocation(Shader_programm, "Ks")
    glUniform3fv(Ks_loc, 1, Ks)

    #expoente expecular
    especular_exp = n
    especular_exp_loc = glGetUniformLocation(Shader_programm, "especular_exp")
    glUniform1f(especular_exp_loc, especular_exp)

def especificaLuz():
    global Shader_programm,luzinha
    #posição da luz
    luz_posicao = np.array([10.0, 10.0, 10.0])
    luz_posicaoloc = glGetUniformLocation(Shader_programm, "luz_posicao")#envia o array da posição da luz para o shader
    glUniform3fv(luz_posicaoloc, 1, luz_posicao)

    #Fonte de luz ambiente [0.2, 0.2, 0.2]
    La = np.array([0.2, 0.2, 0.2])
    La_loc = glGetUniformLocation(Shader_programm, "La")#envia o array da Luz Ambiente para o shader
    glUniform3fv(La_loc, 1, La)

    #Fonte de luz difusa [0.7, 0.7, 0.7]
    Ld = np.array([luzinha])
    Ld_loc = glGetUniformLocation(Shader_programm, "Ld")#envia o array da Luz Difusa para o shader
    glUniform3fv(Ld_loc, 1, Ld)
    
    #Fonte de luz especular [1.0, 1.0, 1.0]
    Ls = np.array([luzinha])
    Ls_loc = glGetUniformLocation(Shader_programm, "Ls")#envia o array da Luz Especular para o shader
    glUniform3fv(Ls_loc, 1, Ls)

def inicializaRenderizacao():
    global Window, Shader_programm, Vao, WIDTH, HEIGHT, Tempo_entre_frames, rotY

    tempo_anterior = glfw.get_time()

    #Ativação do teste de profundidade. Sem ele, o OpenGL não sabe que faces devem ficar na frente e que faces devem ficar atrás.
    glEnable(GL_DEPTH_TEST)
    while not glfw.window_should_close(Window):

        #calcula quantos segundos se passaram entre um frame e outro
        tempo_frame_atual = glfw.get_time()
        Tempo_entre_frames = tempo_frame_atual - tempo_anterior
        tempo_anterior = tempo_frame_atual

        #limpa a tela e os buffers
        glClearColor(0.2, 0.3, 0.3, 1.0)        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #configura a viewport para pegar toda a janela
        glViewport(0, 0, WIDTH, HEIGHT)

        #ativa o shader
        glUseProgram(Shader_programm)
        ativaTextura()
        especificaLuz() #parâmetros da fonte de luz

        inicializaCamera()#configuramos a câmera
        glBindVertexArray(Vao) #ativamos o objeto (cubo) que queremos renderizar

        #objeto
                                #cor ambiente  #cor difusa   #cor especular #n 
        especificaMaterialCubo(0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 1) #parâmetros do material do objeto
        transformaCubo(0,0,0,1,1,1,0,rotY,0) #modifica os parâmetros de transformações geométricas para o cubo
        glDrawArrays(GL_TRIANGLES, 0, indicesVertices) #renderiza o cubo

        glfw.poll_events()

        glfw.swap_buffers(Window)
        
        trataTeclado()

    glfw.terminate()

# Função principal
def main():
    leituraObj("CasaPortaAberta.obj")
    leituraObj("Luminaria.obj")
    leituraObj("Mesa.obj")
    leituraObj("Poste.obj")
    #leituraObj("Sofa.obj")
    inicializaOpenGL()
    inicializaTexturas()
    inicializaObjetos()
    inicializaShaders()
    inicializaRenderizacao()

if __name__ == "__main__":
    main()