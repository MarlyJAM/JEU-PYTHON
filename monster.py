import pygame

#creation de la classe qui gerera nos monstres
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,250)
        self.rect.y = 540
        self.velocity = 1


    def damage(self,amount):
        #infliger des degats

        self.health -= amount

        #verifier si son nombre de point de vie est > ou = à 0
        if self.health <= 0 :
            #reapparaitre comme un nouveau monstre
            self.rect.x = 1000
            self.health = self.max_health
            self.velocity =1


    def update_health_bar(self,surface):
        #desssiner notre bar de vie
        pygame.draw.rect(surface, (115, 115, 115 ), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (9, 225, 120), [self.rect.x + 10 , self.rect.y - 20, self.health ,5])

    def forward(self):
        # le deplacement ne peut etre effectuer que s'il n'ya pas collisions avec le joueur
        if not self.game.check_collisions(self,self.game.all_players) :
            self.rect.x -= self.velocity

        # si le monstre est en collision avec le joueur

        else:
            # infliger des degats au joueur
            self.game.player.damage(self.attack)