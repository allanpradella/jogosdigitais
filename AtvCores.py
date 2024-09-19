import pygame
import random

pygame.init()

#tela teste padrão
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Formas Geométricas com Cores do Arco-Íris")

#f de retângulo
def criar_retangulo(altura, largura, cor, posicao):
    retangulo = pygame.Rect(posicao[0], posicao[1], largura, altura)
    return retangulo, cor

#f de circulo
def criar_circulo(raio, cor, posicao):
    return (posicao[0], posicao[1], raio), cor

#arco iris
cores_arco_iris = [
    (255, 0, 0),    #vermelho
    (255, 127, 0),  #laranja
    (255, 255, 0),  #amarelo
    (0, 255, 0),    #verde
    (0, 0, 255),    #azul
    (75, 0, 130),   #roxo
    (148, 0, 211)    #violeta
]

#lerp
def lerp(value1, value2, factor):
    return value1 + (value2 - value1) * factor

#inter lerp
def lerp_cor(cor1, cor2, t):
    return (
        int(lerp(cor1[0], cor2[0], t)),
        int(lerp(cor1[1], cor2[1], t)),
        int(lerp(cor1[2], cor2[2], t))
    )

#formas aleatórias
formas = []
for _ in range(10):  # in range pra 10 cores
    if random.choice([True, False]):
        altura = random.randint(50, 100)
        largura = random.randint(50, 100)
        cor = random.choice(cores_arco_iris)
        posicao = (random.randint(0, largura_tela - largura), random.randint(0, altura_tela - altura))
        formas.append(criar_retangulo(altura, largura, cor, posicao))
    else:
        raio = random.randint(20, 50)
        cor = random.choice(cores_arco_iris)
        posicao = (random.randint(0, largura_tela - raio * 2), random.randint(0, altura_tela - raio * 2))
        formas.append(criar_circulo(raio, cor, posicao))

#6 retangulos
retangulos = []
num_retangulos = 6
largura_retangulo = largura_tela // num_retangulos
for i in range(num_retangulos):
    cor = random.choice(cores_arco_iris)
    posicao = (i * largura_retangulo, 0)
    retangulos.append(criar_retangulo(altura_tela, largura_retangulo, cor, posicao))

#loop
executando = True
t = 0
incremento = 0.00001  #velocidade 

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    t += incremento
    if t > 1:
        t = 0

    tela.fill((255, 255, 255))  #limpa tela

    mouse_x, mouse_y = pygame.mouse.get_pos()

    #retangulos com interpolação
    for i, (retangulo, cor) in enumerate(retangulos):
        #interpol de cores
        cor_atual = lerp_cor(cor, random.choice(cores_arco_iris), t)
        if retangulo.collidepoint(mouse_x, mouse_y):
            #interpol a partir do mouse
            cor_atual = random.choice(cores_arco_iris)
        pygame.draw.rect(tela, cor_atual, retangulo)

    #criar formas aleatórias
    for forma in formas:
        if isinstance(forma[0], pygame.Rect):
            pygame.draw.rect(tela, forma[1], forma[0])  #retângulo
        else:
            pygame.draw.circle(tela, forma[1], (forma[0][0] + forma[0][2] // 2, forma[0][1] + forma[0][2] // 2), forma[0][2])  #círculo

    pygame.display.flip()

pygame.quit()
