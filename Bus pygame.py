import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Bus game")
eta = pygame.time.Clock()
font = pygame.font.Font(None, 70)

bus = pygame.image.load('bus.png').convert()
bus_anim = 339.375
ground = pygame.image.load('ground.png').convert()
path = pygame.image.load('path.png').convert_alpha()
text = font.render('a', False, 'Red')
gamesound = pygame.mixer.Sound("Bus_loop_one_hour.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bus_anim = bus_anim - 9.84375
                break
            elif event.key == pygame.K_RIGHT:
                bus_anim = bus_anim + 9.84375
                break
    screen.blit(ground, (200, 0))
    screen.blit(path, (400, 0))
    screen.blit(bus, (bus_anim, 60))
    screen.blit(text, (0, 426))
    gamesound.play()
    pygame.display.update()
    eta.tick(60)
    if bus_anim == 378.75:
        pygame.quit()
        exit()
    elif bus_anim == 300:
        pygame.quit()
        exit()
    else:
        continue
