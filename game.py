import pygame.sprite

from player import Player

from monster import Monster

#creer une classe qui va generer notre jeu

class Game:
    def __init__(self):
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()

        self.spawn_monster()
        self.spawn_monster()


        self.pressed = {}

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collisions (self,sprite,group) :
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
