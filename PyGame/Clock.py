import pygame
from math import pi, cos, sin
import datetime

# Constants
WIDTH, HEIGHT = 1520, 720
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 350

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def numbers(number, size, position):
    font = pygame.font.SysFont("Arial", size, True, False)
    text = font.render(number, True, WHITE)
    text_rec = text.get_rect(center=(position))
    screen.blit(text, text_rec)

def polar_to_cartesian(r, theta):
    """ Convert polar coordinates (r, theta) to Cartesian coordinates. """
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)

def main():
    run = True
    while run:
        screen.fill(BLACK)  # Clear the screen before drawing
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Get current time
        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour
        day = current_time.day
        month = current_time.month
        year = current_time.year
        weekday = current_time.isoweekday()

        # Draw the clock face
        pygame.draw.circle(screen, WHITE, center, clock_radius - 10, 10)  # Clock border
        pygame.draw.circle(screen, WHITE, center, 12)  # Center dot
        
        # Clock face
        pygame.draw.rect(screen , WHITE, [WIDTH /2 -260 , HEIGHT/2-30, 80, 60],1)
        pygame.draw.rect(screen , WHITE, [WIDTH /2 -180 , HEIGHT/2-30, 80, 60],1)
        pygame.draw.rect(screen , WHITE, [WIDTH /2 +100 , HEIGHT/2-30, 80, 60],1)
        pygame.draw.rect(screen , WHITE, [WIDTH /2 +180 , HEIGHT/2-30, 80, 60],1)
        pygame.draw.rect(screen , WHITE, [WIDTH /2 -50 , HEIGHT/2-30+160, 100, 60],1)
        # Update display
        pygame.display.update()
        clock.tick(FPS)  # Control frame rate
    pygame.quit()
main()
