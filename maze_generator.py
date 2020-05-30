# Maze generation using recursive backtracker algorithm
# https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker

from queue import LifoQueue
from PIL import Image
import numpy as np
from random import choice


def generate_maze(width, height):
    maze = Image.new('RGB', (width * 2 + 1, height * 2 + 1), 'black')
    pixels = maze.load()

    # Create a path on the very top and bottom so that it has an entrance/exit
    pixels[1, 0] = (255, 255, 255)
    pixels[-2, -1] = (255, 255, 255)
    
    stack = LifoQueue()
    cells = np.zeros((width, height))
    cells[0, 0] = 1
    stack.put((0, 0))

    while not stack.empty():
        x, y = stack.get()

        adjacents = []
        if x > 0 and cells[x - 1, y] == 0:
            adjacents.append((x - 1, y))
        if x < width - 1 and cells[x + 1, y] == 0:
            adjacents.append((x + 1, y))
        if y > 0 and cells[x, y - 1] == 0:
            adjacents.append((x, y - 1))
        if y < height - 1 and cells[x, y + 1] == 0:
            adjacents.append((x, y + 1))

        if adjacents:
            stack.put((x, y))

            neighbour = choice(adjacents)
            neighbour_on_img = (neighbour[0] * 2 + 1, neighbour[1] * 2 + 1)
            current_on_img = (x * 2 + 1, y * 2 + 1)
            wall_to_remove = (neighbour[0] + x + 1, neighbour[1] + y + 1)

            pixels[neighbour_on_img] = (255, 255, 255)
            pixels[current_on_img] = (255, 255, 255)
            pixels[wall_to_remove] = (255, 255, 255)

            cells[neighbour] = 1
            stack.put(neighbour)
    return maze


if __name__ == '__main__':
    w = 23
    h = 15
    my_maze = generate_maze(w, h)
    my_maze.save('maze_' + str(w * 2 + 1) + 'x' + str(h * 2 + 1) + '.png')
