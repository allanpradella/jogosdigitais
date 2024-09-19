import pygame
import math  

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self, name, image_path, initial_position):
        super().__init__()  #Construtor da classe pai
        self.direction = 0  #Direção inicial em graus
        self.name = name
        self.image = pygame.image.load(image_path)  #Load da imagem
        self.original_image = self.image  #Armazena a imagem original
        self.rect = self.image.get_rect()  #Representação do retângulo
        self.rect.center = initial_position  # osição inicial
        self.speed = 5  #Velocidade
        self.shield = 100  #Escudo
        self.energy = 100  #Energia
        self.alive = True  #Status

    def update(self):
        keys = pygame.key.get_pressed()  #Verifica os botões

        #Movimentação baseada em teclas pressionadas
        if keys[pygame.K_LEFT]:
            self.direction -= 5  #Ajusta a direção para a esquerda
        if keys[pygame.K_RIGHT]:
            self.direction += 5  #Ajusta a direção para a direita

        #Cálculo de novas coordenadas com base na direção e velocidade
        radians = math.radians(self.direction)
        dx = math.cos(radians) * self.speed
        dy = math.sin(radians) * self.speed
        self.rect.x += dx
        self.rect.y += dy

        #Limita o movimento dentro da tela
        self.rect.clamp_ip(pygame.Rect(0, 0, 800, 600))

        #Atualiza a imagem rotacionada
        self.image = pygame.transform.rotate(self.original_image, self.direction)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen):  #Desenha a nave
        screen.blit(self.image, self.rect)