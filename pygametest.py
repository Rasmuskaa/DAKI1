import pygame

pygame.init()  # Initialize Pygame
# Create a window of 640x480 pixels
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))  # Fill the screen with white

pygame.draw.line(screen, (0, 0, 0), (100, 380),
                 (540, 380))  # Draw a black line i bunden

pygame.draw.line(screen, (0, 0, 0), (100, 100),
                 (100, 380))  # Draw a black line til venstre

pygame.draw.line(screen, (0, 0, 0), (100, 100),
                 (540, 100))  # Draw a black line i vandrette linje til højre

pygame.draw.line(screen, (0, 0, 0), (540, 100),
                 (540, 380))  # Draw a black line til højre

pygame.draw.line(screen, (0, 0, 0), (310, 0),
                 (540, 100))  # Draw a black line taget til højre

pygame.draw.line(screen, (0, 0, 0), (310, 0),
                 (100, 100))  # Draw a black line taget til venstre

pygame.draw.line(screen, (0, 0, 0), (280, 380),
                 (280, 250))  # Draw a black line dørlinje til venstre

pygame.draw.line(screen, (0, 0, 0), (360, 380),
                 (360, 250))  # Draw a black line dørlinje til højre


pygame.draw.line(screen, (0, 0, 0), (280, 250),
                 (360, 250))  # Draw a black line i bunden linjen over døren


GREEN = (0, 255, 0)

#  (x=, y=, bredde, højde
pygame.draw.rect(screen, GREEN, (0, 380, 820, 100))

BLUE = (0, 0, 255)
pygame.draw.rect(screen, BLUE, (140, 180, 90, 90))
pygame.draw.rect(screen, BLUE, (410, 180, 90, 90))

# Draw the ground
# Draw the bottom of the house
# Draw two walls
# Draw the roof

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip()  # Refresh the screen so drawing appears
