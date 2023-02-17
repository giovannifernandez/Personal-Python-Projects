import pygame
import random

# Initialize pygame
pygame.init()

# Define the game window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Set up the game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define the game variables
CELL_SIZE = 10
FPS = 15

# Define the Snake class
class Snake:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.dx = CELL_SIZE
        self.dy = 0
        self.length = 1
        self.body = [(self.x, self.y)]
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            del self.body[0]
    
    def change_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy
    
    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(game_window, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
    
    def check_collision(self):
        if self.x < 0 or self.x >= WINDOW_WIDTH or self.y < 0 or self.y >= WINDOW_HEIGHT:
            return True
        for x, y in self.body[:-1]:
            if self.x == x and self.y == y:
                return True
        return False

# Define the Food class
class Food:
    def __init__(self):
        self.x = random.randrange(0, WINDOW_WIDTH, CELL_SIZE)
        self.y = random.randrange(0, WINDOW_HEIGHT, CELL_SIZE)
    
    def draw(self):
        pygame.draw.rect(game_window, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))

# Initialize the Snake and Food objects
snake = Snake()
food = Food()

# Define the game loop
clock = pygame.time.Clock()
game_over = False
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.change_direction(-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(CELL_SIZE, 0)
            elif event.key == pygame.K_UP:
                snake.change_direction(0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, CELL_SIZE)
    
    # Move the Snake
    snake.move()
    
    # Check for collision with the Food
    if snake.body[-1][0] == food.x and snake.body[-1][1] == food.y:
        snake.length += 1
        food = Food()
    
    # Check for collision with the walls and the Snake's body
    if snake.check_collision():
        game_over = True
    
    # Draw the game objects
    game_window.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.update()
    
    # Set the FPS
    clock.tick(FPS)

# Clean up the game
pygame.quit()