import sys, pygame
import itchy
pygame.init()

size = width, height = 1000, 1001

black = 0,0,0

screen = pygame.display.set_mode(size)

itchy = itchy.Itchy(width,height)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            itchy.run()
        
    screen.fill(black)
    screen.blit(itchy.get_image(), itchy.get_rect())
    pygame.display.flip()
