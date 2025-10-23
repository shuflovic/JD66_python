import pygame
import sys

# Initialize pygame
pygame.init()

# Settings
WINDOW_SIZE = 500
BOARD_SIZE = 5
SQUARE_SIZE = WINDOW_SIZE // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Create window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Board Game")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill background
    screen.fill(WHITE)
    
    # Draw 5x5 board
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 2)  # Border
            pygame.draw.rect(screen, GRAY, rect)      # Fill
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()