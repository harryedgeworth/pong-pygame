import pygame
import sys

from ball import Ball
from paddle import Paddle

pygame.init()

def handleEvents(evt):
    if evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if evt.key == pygame.K_DOWN:
            player.speed += 7
        if evt.key == pygame.K_UP:
            player.speed -= 7

    if event.type == pygame.KEYUP:
        if evt.key == pygame.K_DOWN:
            player.speed -= 7
        if evt.key == pygame.K_UP:
            player.speed += 7

WIDTH = 800
HEIGHT = 600
FPS = 60
LIGHT_GREY = (100, 100, 100)
GAME_FONT = pygame.font.Font("PressStart2P-Regular.ttf", 26)
OTHER_FONT = pygame.font.Font("PressStart2P-Regular.ttf", 16)

running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

ball = Ball(LIGHT_GREY)
player = Paddle(LIGHT_GREY, 20, HEIGHT/2, 1)
opponent = Paddle(LIGHT_GREY, WIDTH - 20, HEIGHT/2, 2)

all_sprites.add(ball, player, opponent)

while running:
    for event in pygame.event.get():
        handleEvents(event)
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update(ball, player, opponent)

    # Draw / render
    screen.fill(pygame.Color('grey12'))
    pygame.draw.aaline(screen, LIGHT_GREY, (WIDTH/2, 0), (WIDTH/2, HEIGHT))

    # In-game text elements
    player_text = GAME_FONT.render(f"{player.score}", True, LIGHT_GREY)
    opponent_text = GAME_FONT.render(f"{opponent.score}", True, LIGHT_GREY)
    fps_counter = OTHER_FONT.render(f"{int(clock.get_fps())} FPS", True, LIGHT_GREY)
    screen.blit(player_text, (356, 285))
    screen.blit(opponent_text, (422, 285))
    screen.blit(fps_counter, (10, 10))

    all_sprites.draw(screen)

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
sys.exit()
