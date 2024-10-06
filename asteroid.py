from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    angle = random.uniform(20, 50)

    vector_a = self.velocity.rotate(angle)
    vector_b = self.velocity.rotate(-angle)

    new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
    child1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
    child2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

    child1.velocity = vector_a * 1.2
    child2.velocity = vector_b * 1.2
    
    