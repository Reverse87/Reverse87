import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1440, 720))
pygame.display.set_caption("Bus game")
eta = pygame.time.Clock()
font = pygame.font.Font(None, 70)

bus = pygame.image.load('REF/bus/busOG.png').convert()
bus_anim = 660
background = pygame.image.load('REF/bus/groundOG.png').convert()
lines = pygame.image.load('REF/bus/linesOG.png').convert_alpha()
text = font.render('a', False, 'Red')
gamesound = pygame.mixer.Sound("REF/bus/Bus_loop_one_hour.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bus_anim = bus_anim - 20
                break
            elif event.key == pygame.K_RIGHT:
                bus_anim = bus_anim + 20
                break
    screen.blit(background, (0, 0))
    screen.blit(lines, (720, 0))
    screen.blit(bus, (bus_anim, 300))
    screen.blit(text, (0, 675))
    gamesound.play()
    pygame.display.update()
    eta.tick(60)
    if bus_anim == 980:
        pygame.quit()
        exit()
    elif bus_anim == 400:
        pygame.quit()
        exit()
    else:
        continue
