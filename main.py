import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable, asteroids
    Shot.containers = shots, updatable, drawable
    AsteroidField.containers = updatable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for entity in updatable:
            entity.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()

            for bullet in shots:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.kill()
            
        screen.fill("black")
        
        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()