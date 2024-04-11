import pygame

resolution = (800, 800)
screen = pygame.display.set_mode(resolution)
mapSize = (10, 10)  # (rows, columns)
line_width = 2
clock = pygame.time.Clock()  # to set max FPS

def evaluate_dimensions():
    # Evaluate the width and the height of the squares.
    squareWidth = (resolution[0] / mapSize[0]) - line_width * ((mapSize[0] + 1) / mapSize[0])
    squareHeight = squareWidth
    return (squareWidth, squareHeight)

def convert_column_to_x(column, squareWidth):
    x = line_width * (column + 1) + squareWidth * column
    return x

def convert_row_to_y(row, squareHeight):
    y = line_width * (row + 1) + squareHeight * row
    return y

def draw_squares():
     for i in range(mapSize[0]):
        for n in range(mapSize[1]): 
            if (i + n) % 2 == 0:
                fill ("#FADCE4")    
            else:
                fill ("#F4BAD0")
            rect(x + i * squareHeight, y + n *squareHeight, squareHeight, squareHeight)
   

while True:
    clock.tick(60)  # max FPS = 60
    screen.fill(("#FFFFFF"))  # Fill screen with black color.
    draw_squares()
    pygame.display.flip()  # Update the screen.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()