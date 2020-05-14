import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, pid):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 140))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 0
        self.score = 0
        self.id = pid

    def update(self, ball, player, opponent):
        self.rect.y += self.speed

        # Stop paddles from leaving the window
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

        # Opponent AI
        if self.id == 2:
            if self.rect.top < ball.rect.y:
                self.rect.top += 7
            if self.rect.bottom > ball.rect.y:
                self.rect.bottom -= 7
