# Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".
# Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".
# The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:
#
# A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
# A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
#
# All of the lights update simultaneously; they all consider the same current state before moving to the next.
#
# In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
#
# In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?

class Life():

    def __init__(self):

        self.grid = {}

    # create initial grid
    def add_row(self, row, string):

        for i in range(len(string)):
            coord = (i,row)
            self.grid[coord] = string[i]

    # count neighbors of single light
    def count_neigbours(self, coord):

        x = coord[0]
        y = coord[1]
        vector_x = [1,1,0,-1,-1,-1,0,1]
        vector_y = [0,1,1,1,0,-1,-1,-1]
        count = 0
        for i in range(8):
            x_n = x + vector_x[i]
            y_n = y + vector_y[i]
            if (x_n,y_n) in self.grid:
                if self.grid[(x_n,y_n)] == '#':
                    count += 1
        return count

    # implement one step
    def move(self):

        new_grid = {}
        for y in range(100):
            for x in range(100):
                coord = (x, y)
                neighbors_num = self.count_neigbours(coord)
                # change of rules for corners
                if (x == 0 or x == 99) and (y == 0 or y == 99):
                    new_grid[coord] = '#'
                else:
                    if self.grid[coord] == '#':
                        if neighbors_num == 2 or neighbors_num == 3:
                            new_grid[coord] = '#'
                        else:
                            new_grid[coord] = '.'
                    else:
                        if neighbors_num == 3:
                            new_grid[coord] = '#'
                        else:
                            new_grid[coord] = '.'
        self.grid = new_grid

    # count lights of curent grid
    def count_lights(self):

        count = 0
        for y in range(100):
            for x in range(100):
                coord = (x, y)
                if self.grid[coord] == '#':
                    count += 1
        return count

# init game of life
game = Life()
row = 0
try:
    while True:
        string = input()
        game.add_row(row,string)
        row += 1
except EOFError:
    pass

# make number of steps
for i in range(100):
    game.move()

print(game.count_lights())
