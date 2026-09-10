import pygame
WIDTH, HEIGHT, FPS = 800, 600, 60
BLACK= (0, 0, 0)
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