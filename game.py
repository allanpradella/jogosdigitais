import pygame

pygame.init()

#padrão tela teste
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Space Shooter")

#escolha cores
preto = (0, 0, 0)
branco = (255, 255, 255)

#imagem da nave
nave_imagem = pygame.image.load("nave.png")

#classe da nave
class Nave(pygame.sprite.Sprite): #definição classe nave - herdando de pygame.sprite.Sprite
    def __init__(self): #construtor
        super().__init__()
        self.original_image = pygame.image.load("nave.png") #img nave
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width() * 0.2, self.original_image.get_height() * 0.2)) #redimensionando a nave
        self.rect = self.image.get_rect() #cria o retângulo pra definir limites da imagem
        self.rect.centerx = largura_tela // 2 #define a posicção inicial da nave no centro
        self.rect.bottom = altura_tela - 20 #centro horizonatal da tela
        self.velocidade = 5 #velocidade de movimento

#métodos para mover para a esquerda e direita
    def mover_esquerda(self):
        self.rect.x -= self.velocidade
        if self.rect.left < 0:
            self.rect.left = 0

    def mover_direita(self):
        self.rect.x += self.velocidade
        if self.rect.right > largura_tela:
            self.rect.right = largura_tela

#cria a instância da classe nave
nave = Nave()

#loop do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    #verif as teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        nave.mover_esquerda()
    if teclas[pygame.K_RIGHT]:
        nave.mover_direita()

    #atualização da tela
    tela.fill(preto)
    tela.blit(nave.image, nave.rect)
    pygame.display.flip()

    #limite de fps
    pygame.time.Clock().tick(60)

#fecha o jogo
pygame.quit()