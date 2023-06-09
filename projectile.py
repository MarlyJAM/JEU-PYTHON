import pygame

#definition de la classe qui va gerer les projectiles
class Projectile(pygame.sprite.Sprite):
    #definition du projecteur
    def __init__(self,player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x+120
        self.rect.y = player.rect.y+80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 30
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self) :
        self.rect.x += self.velocity
        self.rotate()

        #verifier que le projectile n'entre pas en collision avec un monstre

        for monster in  self.player.game.check_collisions(self,self.player.game.all_monsters) :
            self.remove()
            #infliger des degats au monstre
            monster.damage(self.player.attack)

        #verifier que notre projectile n'est plus present sur l'ecran
        if self.rect.x > 1080 :
            #supprimer le projectile (s'il est situé en dehors de l'ecran)
            self.remove()
