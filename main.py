# Imports
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scorepopup import ScorePopup

# Main 
def main():
    pygame.init()
    font = pygame.font.SysFont(None, 36)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score_popups = []
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = 0
    
    # Delta Time
    dt = 0

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)  

        for popup in score_popups:
            popup.update(dt)
            score_popups = [p for p in score_popups if not p.is_dead()]

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    points = asteroid.get_score()
                    score += points
                    score_popups.append(ScorePopup(asteroid.position, points))

        screen.fill("black")

        # Score
        score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surface, (20, 20))

        # Drawing Objects
        for object in drawable:
            object.draw(screen)

        # Score Pop Up
        for popup in score_popups:
            popup.draw(screen)

        pygame.display.flip()

        # Limit Framerate to 60 FPS
        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()
