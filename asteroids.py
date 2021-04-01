
import pygame

def main():
    screen_dimensions = (800, 600)
    
    pygame.init()
    screen = pygame.display.set_mode(screen_dimensions)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()

if __name__=='__main__':
    main()
