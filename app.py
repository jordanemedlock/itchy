import time
import sys, pygame
import itchy
pygame.init()

size = width, height = 1000, 1001

background_color = 255,255,255

screen = pygame.display.set_mode(size)

itchy = itchy.Itchy(width,height)
while True:
    events = pygame.event.get()
    for event in events:
        print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
            itchy.run(event)
            for func in itchy.queue:
                func(itchy)
                time.sleep(0.03)
                screen.fill(background_color)
                screen.blit(itchy.get_image(), itchy.get_rect())
                pygame.display.flip()
            itchy.queue = []

        
    screen.fill(background_color)
    screen.blit(itchy.get_image(), itchy.get_rect())
    pygame.display.flip()
