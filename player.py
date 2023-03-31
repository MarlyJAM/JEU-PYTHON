import pygame
pygame.init()

from projectile import Projectile
#creation de la class player

class Player(pygame.sprite.Sprite):


    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health=100
        self.max_health=100
        self.attack=10
        self.velocity = 3
        self.image=pygame.image.load('assets/player.png')
        self.all_projectiles = pygame.sprite.Group()
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=500

    def damage(self,amount):
        if self.health - amount > amount :
            self.health -= amount

    def update_health_bar(self,surface):
        #desssiner notre bar de vie
        pygame.draw.rect(surface, (115, 115, 115 ), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (9, 225, 120), [self.rect.x + 50, self.rect.y + 20, self.health ,7])


    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))


    def move_right(self):
        #se deplacer à droite  ,si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collisions(self,self.game.all_monsters) :
            self.rect.x +=self.velocity




    def move_left(self):
        #se deplacer à gauche
        self.rect.x -=self.velocity
