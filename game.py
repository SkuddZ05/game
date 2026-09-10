import pygame
import sys
WIDTH, HEIGHT, FPS = 1945, 1025, 95
BLACK= (0, 0, 0)

BG_COLOR = (20, 20, 30)        # Dark blue/grey
BAR_BG_COLOR = (45, 45, 60)    # Empty bar color
BAR_FILL_COLOR = (0, 255, 150) # Bright green progress color
TEXT_COLOR = (255, 255, 255)

font = pygame.font.SysFont("Arial", 30)



def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Southern Velocity")
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    run_game()
 # Loading Screen
