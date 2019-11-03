import pygame as pg
import sys

# constants
SCREEN_SIZE = (640, 480)
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPEED = 5
HERO_SIZE = 40


def run():
    # Affichage de la fenêtre
    screen = pg.display.set_mode(SCREEN_SIZE)
    # Clock
    clock = pg.time.Clock()
    # Le hero, un carré noir
    hero = pg.Rect(SCREEN_SIZE[0]/2 - HERO_SIZE/2, SCREEN_SIZE[1]/2 - HERO_SIZE/2, HERO_SIZE, HERO_SIZE)

    while True:
        # exit
        if pg.event.get(pg.QUIT): break
        # events queuee
        pg.event.pump()

        # mouvements
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]: hero.move_ip(0, -SPEED)
        if keys[pg.K_DOWN]: hero.move_ip(0, SPEED)
        if keys[pg.K_LEFT]: hero.move_ip(-SPEED, 0)
        if keys[pg.K_RIGHT]: hero.move_ip(SPEED, 0)

        # ne pas sortir du cadre
        hero.clamp_ip(screen.get_rect())
        # afficher le fond et le hero
        screen.fill(BLACK)
        pg.draw.rect(screen, WHITE, hero)
        pg.display.flip()
        # 60 fps
        clock.tick(FPS)






if __name__ == "__main__":
    pg.init()
    run()
    pg.quit()
    sys.exit()