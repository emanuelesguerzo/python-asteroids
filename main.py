# Imports
import pygame
from constants import *
from player import Player

# Main 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Delta Time
    dt = 0

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)  

        screen.fill("black")

        # Drawing Objects
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # Limit Framerate to 60 FPS
        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()
