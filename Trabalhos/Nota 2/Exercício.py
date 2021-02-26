import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

Window = None
Shader_programm_1 = None
Shader_programm_2 = None
Vao = None
WIDTH = 800
HEIGHT = 600

Tx = 0
Ty = 0
Angulo = 0
Sx = 1
Sy = 1
QualShader = 1

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

    print("Placa de vídeo: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    print("Versão do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))

def inicializaObjetos():

    global Vao
    # Vao do quadrado
    Vao = glGenVertexArrays(1)
    glBindVertexArray(Vao)

    # VBO dos vértices do quadrado
    points = [
        # triângulo 1
		0.5, 0.5, 0.0, #vertice superior direito
		0.5, -0.5, 0.0, #vertice inferior direito
		-0.5, -0.5, 0.0, #vertice inferior esquerdo
		#triângulo 2
		-0.5, 0.5, 0.0, #vertice superior esquerdo
		0.5, 0.5, 0.0, #vertice superior direito
		-0.5, -0.5, 0.0 #vertice inferior esquerdo
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    # VBO das cores
    cores = [
		#triângulo 1
		1.0, 1.0, 0.0,#amarelo
		0.0, 1.0, 1.0,#ciano
		1.0, 0.0, 1.0,#magenta
		#triângulo 2
		0.0, 1.0, 1.0,#ciano
		1.0, 1.0, 0.0,#amarelo
		1.0, 0.0, 1.0,#magenta
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaShader1():
    global Shader_programm_1
    # Especificação do Vertex Shader (altura e largura multiplicados por 2):
    vertex_shader = """
        #version 400
        layout(location = 0) in vec3 vertex_posicao; //vem da modelagem de um objeto no python
        layout(location = 1) in vec3 vertex_cores; //vem da modelagem de um objeto no python
        uniform mat4 matriz; //matriz 4x4 vem do python, pois ela tem o modificador "uniform"
        out vec3 cores;
        void main () {
            cores = vertex_cores;
            gl_Position = matriz * vec4 (vertex_posicao.x*2, vertex_posicao.y*2, vertex_posicao.z, 1.0);
        }
    """
    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

    # Especificação do Fragment Shader:
    fragment_shader = """
        #version 400
        in vec3 cores;
		out vec4 frag_colour;
		void main () {
		    frag_colour = vec4 (cores, 1.0);
		}
    """
    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
    Shader_programm_1 = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm_1, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm_1, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def inicializaShader2():
    global Shader_programm_2
    # Especificação do Vertex Shader:
    vertex_shader = """
        #version 400
        layout(location = 0) in vec3 vertex_posicao; //vem da modelagem de um objeto no python
        layout(location = 1) in vec3 vertex_cores; //vem da modelagem de um objeto no python
        uniform mat4 matriz; //matriz 4x4 vem do python, pois ela tem o modificador "uniform"
        out vec3 cores;
        void main () {
            cores = vertex_cores;
            gl_Position = matriz * vec4 (vertex_posicao, 1.0);
        }
    """
    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

    # Especificação do Fragment Shader (cores negativas):
    fragment_shader = """
        #version 400
        in vec3 cores;
		out vec4 frag_colour;
		void main () {
		    frag_colour = vec4 (1.0-cores.r, 1.0-cores.g, 1.0-cores.b, 1.0);
		}
    """
    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
    Shader_programm_2 = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm_2, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm_2, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def transformaQuadrado():
    #matriz de translação
    translacao = np.array([
        [1.0, 0.0, 0.0, Tx], #joga o objeto Tx unidades para a direita/esquerda
        [0.0, 1.0, 0.0, Ty], #joga o objeto Ty unidades para cima/baixo
        [0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    #matriz de rotação de Angulo graus em torno do eixo Z
    anguloRad = np.radians(Angulo)
    cos = np.cos(anguloRad)
    sen = np.sin(anguloRad)
    rotacao = np.array([
        [cos, -sen, 0.0, 0.0],
        [sen, cos, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #matriz de escala
    escala = np.array([
        [Sx, 0.0, 0.0, 0.0], #aumenta/diminui a largura do objeto em Sx vezes
        [0.0, Sy, 0.0, 0.0], #aumenta/diminui a altura do objeto em Sy vezes
        [0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    #combinamos as transformacoes, multiplicando as matrizes
    transformacao = (translacao.dot(rotacao.dot(escala)))
    #print(transformacao)
    
    #E passamos a matriz para o Vertex Shader.
    #descobre o endereço de memória (de vídeo) da variável matriz lá no shader
    if QualShader == 1:
        transformLoc = glGetUniformLocation(Shader_programm_1, "matriz")
    else:
        transformLoc = glGetUniformLocation(Shader_programm_2, "matriz")
    #passa os valores da matriz aqui do python para a memória de vídeo no endereço descoberto acima
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transformacao)

def inicializaRenderizacao():
    global Window, Shader_programm_1, Shader_programm_2, Vao, WIDTH, HEIGHT, Tx, Ty, Angulo, Sx, Sy, QualShader

    DESLOC_POR_SEG = 0.5 #transladar de 0.1 pixeis por segundo
    ESCALA_POR_SEG = 0.5 #escalar de 0.1 pixeis por segundo
    ANGULOS_POR_SEG = 20 #rotacionar de 1 pixel por segundo

    tempo_antes = glfw.get_time() #pega a hora do sistema antes do laço


    tempo_shader_ultima_modificacao = glfw.get_time() #pega a hora do sistema antes do laço para garantir 1 troca de shader por segundo no máximo
    while not glfw.window_should_close(Window):
        tempo_atual = glfw.get_time() #pega a hora do sistema agora
        tempo_dif = tempo_atual - tempo_antes
        tempo_antes = tempo_atual
        FPS = 1/tempo_dif
        #print("Passaram ",tempo_dif," segundos e está executando em ",round(FPS)," frames por segundo")

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glViewport(0, 0, WIDTH, HEIGHT)

        if QualShader == 1:
            glUseProgram(Shader_programm_1) #ativa o shader 1
        else:
            glUseProgram(Shader_programm_2) #ativa o shader 2

        glBindVertexArray(Vao) #ativa o objeto a ser renderizado

        transformaQuadrado() #configura o valor da variavel "matriz" do shader, que corresponde a transformações geométricas

        glDrawArrays(GL_TRIANGLES, 0, 6) #renderiza o objeto

        glfw.poll_events()

        glfw.swap_buffers(Window)
        
        #testes de teclado
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_RIGHT)):#pressionou a tecla para direita
            #print("Desloquei ",DESLOC_POR_SEG*tempo_dif)
            Tx+=DESLOC_POR_SEG*tempo_dif

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_LEFT)):#pressionou a tecla para esquerda
            Tx-=DESLOC_POR_SEG*tempo_dif

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_UP)):#pressionou a tecla para cima
            Ty+=DESLOC_POR_SEG*tempo_dif
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_DOWN)):#pressionou a tecla para baixo
            Ty-=DESLOC_POR_SEG*tempo_dif
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_PAGE_UP)):#pressionou a tecla PAGE_UP
            Angulo+=ANGULOS_POR_SEG*tempo_dif

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_PAGE_DOWN)):#pressionou a tecla PAGE_DOWN
            Angulo-=ANGULOS_POR_SEG*tempo_dif

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_INSERT)):#pressionou a tecla INSERT
            Sx+=ESCALA_POR_SEG*tempo_dif
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_DELETE)):#pressionou a tecla DELETE
            Sx-=ESCALA_POR_SEG*tempo_dif

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_HOME)):#pressionou a tecla HOME
            Sy+=ESCALA_POR_SEG*tempo_dif
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_END)):#pressionou a tecla END
            Sy-=ESCALA_POR_SEG*tempo_dif

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_S)):#pressionou a tecla S
            tempo_shader_atual = glfw.get_time() #pega a hora do sistema agora
            tempo_shader_dif = tempo_shader_atual - tempo_shader_ultima_modificacao
            print(tempo_shader_dif)
            if tempo_shader_dif >=0.3: #se passou 0.3 segundo desde a ultima mudança de shader
                tempo_shader_ultima_modificacao = glfw.get_time()
                if QualShader == 1:
                    QualShader = 2
                else:
                    QualShader = 1

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)):
            glfw.set_window_should_close(Window, True)
    
    glfw.terminate()

# Função principal
def main():
    inicializaOpenGL()
    inicializaObjetos()
    inicializaShader1()
    inicializaShader2()
    inicializaRenderizacao()

if __name__ == "__main__":
    main()