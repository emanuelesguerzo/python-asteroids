import pygame

class ScorePopup:
    def __init__(self, position, value):
        self.position = pygame.Vector2(position)
        self.value = value
        self.opacity = 255
        self.lifetime = 1.0  # secondi
        self.font = pygame.font.SysFont(None, 24)

    def update(self, dt):
        self.lifetime -= dt
        self.position.y -= 20 * dt  # si muove verso l’alto
        self.opacity = max(0, int(255 * (self.lifetime / 1.0)))  # fading

    def draw(self, screen):
        surface = self.font.render(f"+{self.value}", True, (255, 255, 255))
        surface.set_alpha(self.opacity)
        screen.blit(surface, self.position)
    
    def is_dead(self):
        return self.lifetime <= 0