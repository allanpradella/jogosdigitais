import random
import time

class NaveEspacial:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.position = (0, 0)  # Posição inicial
        self.direction = 0  # Direção inicial (0 graus)
        self.speed = 0  # Velocidade inicial
        self.shield = 100  # Nível de escudo inicial
        self.energy = 100  # Energia inicial

    def move(self):
        if self.alive:
            print(f"{self.name} está se movendo para a frente.")
        else:
            print(f"{self.name} está destruída e não pode se mover.")

    def turn(self, direction):
        if self.alive:
            if direction.lower() == 'esquerda':
                self.direction -= 90  # Exemplo de rotação
            elif direction.lower() == 'direita':
                self.direction += 90
            print(f"{self.name} virou para a {direction}.")
        else:
            print(f"{self.name} está destruída e não pode girar.")

    def shoot(self):
        if self.alive:
            if self.energy >= 10:
                self.energy -= 10  # Custo de energia para atirar
                print(f"{self.name} lançou um projétil.")
            else:
                print(f"{self.name} não tem energia suficiente para atirar.")
        else:
            print(f"{self.name} está destruída e não pode atirar.")

    def hit(self, damage):
        if self.alive:
            self.shield -= damage
            if self.shield <= 0:
                self.alive = False
                print(f"{self.name} foi destruída.")
            else:
                print(f"{self.name} foi atingida! Escudo restante: {self.shield}")
        else:
            print(f"{self.name} já está destruída.")

    def recharge(self):
        if self.alive:
            self.energy = 100
            print(f"{self.name} recarregou sua energia.")
        else:
            print(f"{self.name} está destruída e não pode recarregar energia.")

def game_loop(player1, player2):
    players = [player1, player2]
    while player1.alive and player2.alive:
        current_player = random.choice(players)
        if random.choice([True, False]):
            current_player.move()
        else:
            current_player.shoot()

        # Chance de recarregar energia aleatoriamente
        if random.random() < 0.1:
            current_player.recharge()

        # Simular dano entre jogadores
        if random.random() < 0.3:
            damage = random.randint(10, 30)
            if current_player == player1:
                player2.hit(damage)
            else:
                player1.hit(damage)

        time.sleep(1)  # Pausa para simular tempo de jogo

    print("Jogo terminado!")

# Exemplo de uso
nave1 = NaveEspacial("Falcon")
nave2 = NaveEspacial("Eagle")

game_loop(nave1, nave2)
