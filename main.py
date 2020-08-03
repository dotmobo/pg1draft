import pygame as pg
import sys
from random import randrange

# constants
SCREEN_SIZE = (640, 480)
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
HERO_SPEED = 5
HERO_SIZE = 40
MONSTER_SIZE_MIN = 10
MONSTER_SIZE_MAX = 40
MONSTER_SPEED = 2
MONSTERS_MIN = 2
MONSTERS_MAX = 6


def run():
    # Affichage de la fenêtre
    screen = pg.display.set_mode(SCREEN_SIZE)
    # Font
    font = pg.font.SysFont(None, 32)
    # Clock
    clock = pg.time.Clock()
    # Timer
    start_time = pg.time.get_ticks()
    counting_time = 0
    # Game over
    game_over = False
    # Le hero, un carré noir
    hero = pg.Rect(SCREEN_SIZE[0]/2 - HERO_SIZE/2, SCREEN_SIZE[1]/2 - HERO_SIZE/2, HERO_SIZE, HERO_SIZE)
    # L ennemi, un carré rouge
    monsters = []
    for i in range(0, randrange(MONSTERS_MIN, MONSTERS_MAX)):
        size = randrange(MONSTER_SIZE_MIN, MONSTER_SIZE_MAX)
        monsters.append(pg.Rect(randrange(SCREEN_SIZE[0]), randrange(SCREEN_SIZE[1]), size, size))


    while True:
        # events queue
        pg.event.pump()
        # mouvements
        keys = pg.key.get_pressed()

        # exit
        if pg.event.get(pg.QUIT) or keys[pg.K_ESCAPE]: break

        if game_over:
            screen.fill(BLACK)
            gameover_text = font.render('GAME OVER - SCORE: {counting_time}'.format(counting_time=counting_time), 1, (255,255,255))
            gameover_rect = gameover_text.get_rect(center=(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2))
            screen.blit(gameover_text, gameover_rect)

            if keys[pg.K_RETURN]:
                # Timer
                start_time = pg.time.get_ticks()
                counting_time = 0
                # Le hero, un carré noir
                hero = pg.Rect(SCREEN_SIZE[0]/2 - HERO_SIZE/2, SCREEN_SIZE[1]/2 - HERO_SIZE/2, HERO_SIZE, HERO_SIZE)
                # L ennemi, un carré rouge
                monsters = []
                for i in range(0, randrange(MONSTERS_MIN, MONSTERS_MAX)):
                    size = randrange(MONSTER_SIZE_MIN, MONSTER_SIZE_MAX)
                    monsters.append(pg.Rect(randrange(SCREEN_SIZE[0]), randrange(SCREEN_SIZE[1]), size, size))
                game_over = False

            

        else:

            # timer
            counting_time = pg.time.get_ticks() - start_time

            
            if keys[pg.K_UP]: hero.move_ip(0, -HERO_SPEED)
            if keys[pg.K_DOWN]: hero.move_ip(0, HERO_SPEED)
            if keys[pg.K_LEFT]: hero.move_ip(-HERO_SPEED, 0)
            if keys[pg.K_RIGHT]: hero.move_ip(HERO_SPEED, 0)

            # suicide
            if keys[pg.K_s]: game_over = True

            # monster moves X
            for monster in monsters:
                if hero.x > monster.x:
                    monster.move_ip(MONSTER_SPEED, 0)
                elif hero.x < monster.x:
                    monster.move_ip(-MONSTER_SPEED, 0)

                if hero.y > monster.y:
                    monster.move_ip(0, MONSTER_SPEED)
                elif hero.y < monster.y:
                    monster.move_ip(0, -MONSTER_SPEED)

                # monster kill
                if (monster.colliderect(hero)):
                    game_over = True

                # ne pas sortir du cadre
                monster.clamp_ip(screen.get_rect())

            
            # ne pas sortir du cadre
            hero.clamp_ip(screen.get_rect())
            # afficher le fond et le hero
            screen.fill(BLACK)
            # Timer
            counting_text = font.render('SCORE: {counting_time}'.format(counting_time=counting_time), 1, (255,255,255))
            counting_rect = counting_text.get_rect()
            screen.blit(counting_text, counting_rect)
            # hero
            pg.draw.rect(screen, WHITE, hero)
            # monster
            for monster in monsters:
                pg.draw.rect(screen, RED, monster)
        
        
        # refresh
        pg.display.flip()
        # 60 fps
        clock.tick(FPS)






if __name__ == "__main__":
    pg.init()
    run()
    pg.quit()
    sys.exit()