import random

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 10
        self.armor = 100

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEAD)" % self.name

    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(f'{self.name} fires on {enemy.name}')
            enemy.hit()
        else:
            print(f'{self.name} has no shells!')

    def hit(self):
        self.armor -= 20
        print(f'{self.name} is hit')
        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(f'{self.name} explodes!')

# Lista para armazenar objetos
tanques = [
    Tank('Allan'),
    Tank('Eduardo'),
    Tank('Felipe'),
    Tank('Melissa'),
    Tank('Hanna')
]

def mostrar_estado_tanques(tanques):
    print(f'CURRENT TANK STATUS:')
    for tanque in tanques:
        print(f'{tanque.name}: {"Alive" if tanque.alive else "DEAD"}, Armor: {tanque.armor}, Ammo: {tanque.ammo}')

def batalha(tanques):
    # Loop para que reste apenas um tanque vivo
    while len([t for t in tanques if t.alive]) > 1:
        tanque_atacante = random.choice([t for t in tanques if t.alive]) # Escolha do tanque atacante
        
        # Criar lista de tanques remanescentes excluindo o tanque atacante
        tanques_remanescentes = [t for t in tanques if t.alive and t != tanque_atacante]
        
        if tanques_remanescentes:
            # Sorteio do tanque alvo
            tanque_alvo = random.choice(tanques_remanescentes)
            
            # O tanque atacante ataca o alvo
            tanque_atacante.fire_at(tanque_alvo)
            
            # Remover o tanque alvo se ele explodir
            if not tanque_alvo.alive:
                tanques.remove(tanque_alvo) # Remover o tanque
        else:
            print('No tanks remaining to be targeted.')

        print() # Separação visual de ataques
        mostrar_estado_tanques(tanques) # Mostrar o estado dos tanques

    if len([t for t in tanques if t.alive]) == 1:
        vencedor = [t for t in tanques if t.alive][0]
        print(f'The winner is {vencedor}!') # Mostrar o vencedor
    else:
        print('Not enough tanks remaining.')

# Executar a simulação
batalha(tanques)
