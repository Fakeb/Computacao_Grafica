# Rafael Meneses e Rafael Cancian - 12/11/2020 - Lista de exercícios - Transformações Geométricas e Shaders
# Transformações geométricas
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

Window = None
Shader_programmP = None
Shader_programmS = None
Vao = None
WIDTH = 800
HEIGHT = 600
eixoX = 0
eixoY = 0
rotacaoXY = 0

newPoints = [

    #triângulo 1
    0.5, 0.5, 0.0, #vertice superior direito
    0.5, -0.5, 0.0, #vertice inferior direito
    -0.5, -0.5, 0.0, #vertice inferior esquerdo
    #triângulo 2
    -0.5, 0.5, 0.0, #vertice superior esquerdo
    0.5, 0.5, 0.0, #vertice superior direito
    -0.5, -0.5, 0.0 #vertice inferior esquerdo

]

pointsSomaSub = [

    #triângulo 1
    0.001, 0.001, 0.0, #vertice superior direito
    0.001, -0.001, 0.0, #vertice inferior direito
    -0.001, -0.001, 0.0, #vertice inferior esquerdo
    #triângulo 2
    -0.001, 0.001, 0.0, #vertice superior esquerdo
    0.001, 0.001, 0.0, #vertice superior direito
    -0.001, -0.001, 0.0 #vertice inferior esquerdo

]

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

def inicializaObjetos(novopoints):

    global Vao
    # Vao do quadrado
    Vao = glGenVertexArrays(1)
    glBindVertexArray(Vao)

    # VBO dos vértices do quadrado
    points = novopoints
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

def inicializaShadersPrincipal():
    global Shader_programmP
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
    Shader_programmP = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programmP, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programmP, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def inicializaShadersSecundario():
    global Shader_programmS
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

    # Especificação do Fragment Shader:
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
    Shader_programmS = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programmS, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programmS, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def transformaQuadrado(x,y,rot):
    #matriz de translação
    translacao = np.array([
        [1.0, 0.0, 0.0, x], #joga o objeto 0.5 unidades para a direita
        [0.0, 1.0, 0.0, y], #joga o objeto 0.5 unidades para baixo
        [0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    #matriz de rotação de 30 graus em torno do eixo Z
    angulo = np.radians(rot)
    cos = np.cos(angulo)
    sen = np.sin(angulo)
    rotacao = np.array([
        [cos, -sen, 0.0, 0.0],
        [sen, cos, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #combinamos as transformacoes, multiplicando as matrizes
    transformacao = (translacao.dot(rotacao))
    #print(transformacao)
    
    #E passamos a matriz para o Vertex Shader.
    #descobre o endereço de memória (de vídeo) da variável matriz lá no shader
    transformLoc = glGetUniformLocation(Shader_programmP, "matriz") 
    #passa os valores da matriz aqui do python para a memória de vídeo no endereço descoberto acima
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transformacao)

def inicializaRenderizacao():
    global Window, Shader_programmP, Shader_programmS, Vao, WIDTH, HEIGHT, eixoX, eixoY, rotacaoXY, newPoints, pointsSomaSub

    shadernovo = Shader_programmP

    while not glfw.window_should_close(Window):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glViewport(0, 0, WIDTH, HEIGHT)

        glUseProgram(shadernovo) #ativa o shader

        glBindVertexArray(Vao) #ativa o objeto a ser renderizado

        #transformaQuadrado() #configura o valor da variavel "matriz" do shader, que corresponde a transformações geométricas
        transformaQuadrado(eixoX,eixoY,rotacaoXY)

        glDrawArrays(GL_TRIANGLES, 0, 6) #renderiza o objeto

        glfw.poll_events()

        glfw.swap_buffers(Window)
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)):
            glfw.set_window_should_close(Window, True)

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_RIGHT)): # DIREITA
            eixoX += 0.001
            transformaQuadrado(eixoX,eixoY,rotacaoXY)
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_LEFT)): # ESQUERDA
            eixoX -= 0.001
            transformaQuadrado(eixoX,eixoY,rotacaoXY)
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_UP)): # CIMA
            eixoY += 0.001
            transformaQuadrado(eixoX,eixoY,rotacaoXY)
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_DOWN)): # BAIXO
            eixoY -= 0.001
            transformaQuadrado(eixoX,eixoY,rotacaoXY)
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_PAGE_DOWN)): # ROTAÇÃO SENTIDO HORARIO
            rotacaoXY += 0.1
            transformaQuadrado(eixoX,eixoY,rotacaoXY)

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_PAGE_UP)): # ROTAÇÃO SENTIDO ANTI-HORARIO
            rotacaoXY -= 0.1
            transformaQuadrado(eixoX,eixoY,rotacaoXY)

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_1)): # expandir
            
            pointsSomaSub = np.add(pointsSomaSub,[#triângulo 1
                0.001, 0.001, 0.0, #vertice superior direito
                0.001, -0.001, 0.0, #vertice inferior direito
                -0.001, -0.001, 0.0, #vertice inferior esquerdo
                #triângulo 2
                -0.001, 0.001, 0.0, #vertice superior esquerdo
                0.001, 0.001, 0.0, #vertice superior direito
                -0.001, -0.001, 0.0 #vertice inferior esquerdo
            ])
            outroPonto = np.add(newPoints, pointsSomaSub)  
            inicializaObjetos(outroPonto)
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_2)): # diminuir
            
            pointsSomaSub = np.subtract(pointsSomaSub,[#triângulo 1
                0.001, 0.001, 0.0, #vertice superior direito
                0.001, -0.001, 0.0, #vertice inferior direito
                -0.001, -0.001, 0.0, #vertice inferior esquerdo
                #triângulo 2
                -0.001, 0.001, 0.0, #vertice superior esquerdo
                0.001, 0.001, 0.0, #vertice superior direito
                -0.001, -0.001, 0.0 #vertice inferior esquerdo
            ])
            outroPonto = np.add(newPoints, pointsSomaSub)  
            inicializaObjetos(outroPonto)

        shadernovo = Shader_programmP

        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_S)): # trocar shader temporariamente
            
            shadernovo = Shader_programmS #ativa o shader

    glfw.terminate()

# Função principal
def main():
    global newPoints
    inicializaOpenGL()
    inicializaObjetos(newPoints)
    inicializaShadersPrincipal()
    inicializaShadersSecundario()
    inicializaRenderizacao()

if __name__ == "__main__":
    main()