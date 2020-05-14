import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (800/2, 600/2)
        self.xspeed = 5 * random.choice((1, -1))
        self.yspeed = 5 * random.choice((1, -1))

    def update(self, ball, player, opponent):
        self.serveBall()

        # Stop the ball from leaving the window
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.xspeed *= -1

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.yspeed *= -1

        # Ball collision detection on Paddles
        if pygame.sprite.collide_rect(self, player):
            ball.xspeed *= -1
        elif pygame.sprite.collide_rect(self, opponent):
            ball.xspeed *= -1

        # Ball hits score area
        if self.rect.left <= 0:
            opponent.score += 1
            self.resetBoard(player, opponent)
        elif self.rect.right >= 800:
            player.score += 1
            self.resetBoard(player, opponent)

    def serveBall(self):
        # TODO: Serve the ball after a short countdown
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

    def resetBoard(self, pl, opp):
        self.__init__(self.color)
        pl.rect.center = (20, 600 / 2)
        opp.rect.center = (780, 600 / 2)
