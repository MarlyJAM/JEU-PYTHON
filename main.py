import pygame
from game import Game

#generer la fenetre du jeu

pygame.display.set_caption("Comet Fall Game")

screen = pygame.display.set_mode((1080,720))

#definir l'arrière plan de notre jeu

background =  pygame.image.load('assets/bg.jpg')

#charger notre jeu

game = Game()

running = True

#boucle tant que running est vrai

while running:
    #appliquer l'arrière plan du jeu

    screen.blit(background,(0,-200))

    #appliquer l'image du joueur

    screen.blit(game.player.image , game.player.rect)

    #actualiser la bar de vie du joueur
    game.player.update_health_bar(screen)

    #recuper les projectiles deja creer

    for projectile in game.player.all_projectiles :
        projectile.move()

    #recuperer les monstres de notre jeu

    for monster in game.all_monsters :
        monster.forward()
        monster.update_health_bar(screen)

    #appliquer l'ensemble des images de mon groupe projectile

    game.player.all_projectiles.draw(screen)

    #appliquer l'ensemble des images de mon groupe monster

    game.all_monsters.draw(screen)

    #mettre à jour la fenetre

    pygame.display.flip()

    #verifier si le joueur veut aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width<screen.get_width():
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0:
        game.player.move_left()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #verifier que l'evenement est sortir
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()

        #detecter si un joueur lache une prise de clavier

        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True
            #quelle touche a été utilisée
            #if event.key == pygame.K_RIGHT:
            #    game.player.move_right()

            #elif event.key == pygame.K_LEFT:
            #    game.player.move_lef()

            #detecter si la touche espace est activer
            if event.key == pygame.K_SPACE :
                game.player.launch_projectile()



        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


