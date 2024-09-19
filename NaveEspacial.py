import pygame

class NaveEspacial(pygame.sprite.Sprite): #representação da nave - construtor
    def __init__(self, name, image_path, initial_position): #inicializa a nave com seus argumentos
        super().__init__() #construtor da classe pai
        self.name = name 
        self.image = pygame.image.load(image_path) #load da imagem 
        self.rect = self.image.get_rect() #representação do retângulo
        self.rect.center = initial_position #posição inicial
        self.speed = 5 #velocidade
        self.shield = 100 #escudo
        self.energy = 100 #energia
        self.alive = True #status

    def update(self): #def pra atualizar posição da nave
        keys = pygame.key.get_pressed() #verifica os botões pra posicionar a nave
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Limitar a nave à tela (ajuste os limites de acordo com sua tela)
        self.rect.clamp_ip(pygame.Rect(0, 0, 800, 600))

    def draw(self, screen): #desenha a nave
        screen.blit(self.image, self.rect)