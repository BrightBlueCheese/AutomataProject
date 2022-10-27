import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400,300))

# Initialing Color
color = (255,0,0)

pygame.draw.rect(surface, color, pygame.Rect(-10, -10, 30, 30), 2)
pygame.display.flip()
# Drawing Rectangle
while True:
    for event in pygame.event.get():

        # when press quit, quit
        if event.type == pygame.QUIT:
            pygame.quit()
            

        # when press space, pause
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running
                pygame.display.update()
