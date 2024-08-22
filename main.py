import pygame # type: ignore
from constants import *
from player import *
pygame.init()


def main () :
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    p = player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2,PLAYER_RADIUS)
    while True : 
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
               return
        
        screen.fill((0,0,0))
        p.update(dt)
        p.draw(screen)
        pygame.display.flip()
        
        time.tick(60)
        dt = time.tick(60)/1000

        
    
if __name__ == "__main__":
    main()


