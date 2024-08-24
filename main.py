import pygame # type: ignore
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *
pygame.init()


def main () :
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids , updatable , drawable)
    player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots ,updatable,drawable)
    p = player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2,PLAYER_RADIUS)
    a =AsteroidField()
    
    while True : 
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
               return
             
        for objects in updatable : 
            objects.update(dt)

        for objects in asteroids : 
            if objects.collision(p) :
                 sys.exit("Game Over!!")

        for objects in asteroids :
            for shot in shots : 
                if objects.collision(shot) :
                    shot.kill()
                    objects.split()

        screen.fill((0,0,0))

        for objects in drawable : 
            objects.draw(screen)

        pygame.display.flip()
        
       
        
        time.tick(60)
        dt = time.tick(60)/1000

        
    
if __name__ == "__main__":
    main()


